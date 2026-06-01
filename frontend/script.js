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

    const graphContainer =
        document.getElementById(
            "graphContainer"
        );

    messages.innerHTML = "";
    graphContainer.innerHTML = "";

    let latestGraph = null;

    chat.messages.forEach(msg=>{

        const div =
            document.createElement(
                "div"
            );

        if(msg.role === "user"){

            div.className =
                "user-message";

            div.innerHTML =
                msg.content;

        }

        else{

            div.className =
                "bot-message";

            if(
                typeof msg.content === "object"
            ){

                div.innerHTML = `

                <h3>
                🏆 Best Model:
                ${msg.content.best_model}
                </h3>

                <p>
                Confidence:
                <b>
                ${msg.content.confidence}%
                </b>
                </p>

                <hr>

                <div>
                ${msg.content.response.replace(
                    /\n/g,
                    "<br>"
                )}
                </div>

                `;

                latestGraph =
                    msg.content.graph;

            }
            else{

                div.innerHTML =
                    msg.content;
            }
        }

        messages.appendChild(
            div
        );

    });

    if(latestGraph){

        renderGraph(
            latestGraph
        );

    }

    messages.scrollTop =
        messages.scrollHeight;
}

function renderGraph(graph){

    const container =
        document.getElementById(
            "graphContainer"
        );

    container.innerHTML = `

    <h2>
    Model Confidence
    </h2>

    `;

    if(!graph)
        return;

    graph.forEach(item=>{

        container.innerHTML += `

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

    if(data.graph){

    renderGraph(
        data.graph
    );

}

    messages.scrollTop =
        messages.scrollHeight;

    await loadChats();
}