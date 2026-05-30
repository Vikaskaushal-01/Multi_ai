const sessionId = "session_1";

window.onload = async () => {

    const prompt = localStorage.getItem(
        "current_prompt"
    );

    if (prompt) {

        document.getElementById(
            "question"
        ).value = prompt;

        await sendMessage();

        localStorage.removeItem(
            "current_prompt"
        );
    }
};


async function sendMessage() {

    const question = document
        .getElementById("question")
        .value;

    const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                session_id: sessionId,
                query: question
            })
        }
    );

    const data = await response.json();

    const messages = document
        .getElementById("messages");

    messages.innerHTML += `
        <div class="user-msg">
            ${question}
        </div>

        <div class="bot-msg">
            <strong>Best Model:</strong>
            ${data.best_model}
            <br><br>
            ${data.response}
        </div>
    `;
}