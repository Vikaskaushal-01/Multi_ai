const API =
"http://127.0.0.1:8000";

let currentChatId = null;

window.onload = async () => {

    await createChat();

    await loadChats();

};

document
.getElementById("newChatBtn")
.addEventListener(

    "click",

    async ()=>{

        await createChat();

        document
        .getElementById("messages")
        .innerHTML = "";

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

        div.innerText =
        msg.content;

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
    ).value;

    if(!question) return;

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

    const messages =
    document.getElementById(
        "messages"
    );

    messages.innerHTML += `

    <div class="user-message">

        ${question}

    </div>

    <div class="bot-message">

        <b>
        Best Model:
        ${data.best_model}
        </b>

        <br><br>

        Confidence:
        ${data.confidence}%

        <br><br>

        ${data.response}

    </div>

    `;

    renderGraph(
        data.graph
    );

    document
    .getElementById(
        "question"
    ).value = "";

    messages.scrollTop =
    messages.scrollHeight;

    await loadChats();
}