function renderGraph(scores) {

    const canvas =
        document.getElementById("graphCanvas");

    if (!canvas) return;

    const ctx =
        canvas.getContext("2d");

    canvas.width = 700;
    canvas.height = 500;

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    const centerX = 350;
    const centerY = 250;

    // Prompt node

    ctx.beginPath();

    ctx.arc(
        centerX,
        centerY,
        35,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = "#2563eb";
    ctx.fill();

    ctx.fillStyle = "#ffffff";
    ctx.font = "14px Arial";

    ctx.fillText(
        "PROMPT",
        centerX - 28,
        centerY + 5
    );

    scores.forEach((item, index) => {

        const angle =
            (index / scores.length) *
            Math.PI *
            2;

        const distance =
            120 +
            (1 - item.score) * 200;

        const x =
            centerX +
            Math.cos(angle) *
            distance;

        const y =
            centerY +
            Math.sin(angle) *
            distance;

        // Connection line

        ctx.beginPath();

        ctx.moveTo(
            centerX,
            centerY
        );

        ctx.lineTo(
            x,
            y
        );

        ctx.strokeStyle =
            "#64748b";

        ctx.stroke();

        // Model node

        ctx.beginPath();

        ctx.arc(
            x,
            y,
            25,
            0,
            Math.PI * 2
        );

        ctx.fillStyle =
            "#10b981";

        ctx.fill();

        ctx.fillStyle =
            "#ffffff";

        ctx.fillText(
            item.model,
            x - 22,
            y + 40
        );

        ctx.fillText(
            (item.score * 100).toFixed(0) + "%",
            x - 12,
            y + 5
        );
    });
}