const sessionId = crypto.randomUUID();

async function sendMessage() {

    const question =
        document.getElementById("question").value;

    const responseDiv =
        document.getElementById("response");

    responseDiv.innerHTML = "Generating...";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({
                    session_id: sessionId,
                    query: question
                })
            }
        );

        const data = await response.json();

        responseDiv.innerHTML =
            data.response;

    } catch {

        responseDiv.innerHTML =
            "Backend connection failed.";

    }
}