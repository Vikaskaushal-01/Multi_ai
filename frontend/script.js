const API =
    "http://127.0.0.1:8000";

let currentChatId = null;

window.onload = async () => {

    await loadChats();

};

document
.getElementById("newChatBtn")
.addEventListener(

    "click",

    async ()=>{

        await createChat();

        document
        .getElementById(
            "messages"
        ).innerHTML = "";

        document
        .getElementById(
            "graphContainer"
        ).innerHTML = "";

    }

);

async function createChat(){

    const response =
        await fetch(

            `${API}/new-chat`,

            {
                method:"POST"
            }

        );

    const data =
        await response.json();

    currentChatId =
        data.chat_id;

    await loadChats();
}

async function loadChats(){

    const response =
        await fetch(
            `${API}/chats`
        );

    const chats =
        await response.json();

    const list =
        document.getElementById(
            "chatList"
        );

    list.innerHTML = "";

    chats.forEach(chat=>{

        const div =
            document.createElement(
                "div"
            );

        div.className =
            "chat-item";

        div.innerText =
            chat.title;

        div.onclick = ()=>{

            currentChatId =
                chat.id;

            loadHistory(chat);

        };

        list.appendChild(div);

    });

    if(
        !currentChatId &&
        chats.length > 0
    ){

        currentChatId =
            chats[0].id;

        loadHistory(
            chats[0]
        );

    }
}

function loadHistory(chat){

    const messages =
        document.getElementById(
            "messages"
        );

    messages.innerHTML = "";

    chat.messages.forEach(msg=>{

        const div =
            document.createElement(
                "div"
            );

        div.className =
            msg.role === "user"
            ? "user-message"
            : "bot-message";

        div.innerHTML =
            msg.content.replace(
                /\n/g,
                "<br>"
            );

        messages.appendChild(
            div
        );

    });

    messages.scrollTop =
        messages.scrollHeight;
}

async function sendMessage(){

    const question =
        document.getElementById(
            "question"
        ).value.trim();

    if(!question)
        return;

    if(!currentChatId){

        await createChat();

    }

    const messages =
        document.getElementById(
            "messages"
        );

    messages.innerHTML += `

    <div class="user-message">

        ${question}

    </div>

    `;

    messages.scrollTop =
        messages.scrollHeight;

    document
    .getElementById(
        "question"
    ).value = "";

    const response =
        await fetch(

            `${API}/chat`,

            {

                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({

                    chat_id:
                    currentChatId,

                    query:
                    question

                })

            }

        );

    const data =
        await response.json();

    messages.innerHTML += `

    <div class="bot-message">

        <h3>

        🏆 Best Model:
        ${data.best_model}

        </h3>

        <p>

        Confidence:

        <b>

        ${data.confidence}%

        </b>

        </p>

        <hr>

        <div>

        ${data.response.replace(/\n/g,"<br>")}

        </div>

    </div>

    `;

    let graphHtml = "";

    data.graph.forEach(item=>{

        graphHtml += `

        <div class="score-row">

            <div class="score-name">

                ${item.model}

            </div>

            <div class="score-bar">

                <div
                    class="score-fill"
                    style="width:${item.percentage}%">
                </div>

            </div>

            <div>

                ${item.percentage}%

            </div>

        </div>

        `;

    });

    document
    .getElementById(
        "graphContainer"
    ).innerHTML = graphHtml;

    messages.scrollTop =
        messages.scrollHeight;

    await loadChats();
}