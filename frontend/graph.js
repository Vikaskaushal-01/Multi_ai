function renderGraph(scores){

    const canvas =
        document.getElementById(
            "graphCanvas"
        );

    const ctx =
        canvas.getContext("2d");

    canvas.width = 700;
    canvas.height = 400;

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    const centerX = 350;
    const centerY = 200;

    ctx.beginPath();

    ctx.arc(
        centerX,
        centerY,
        30,
        0,
        Math.PI*2
    );

    ctx.fillStyle =
        "#2563eb";

    ctx.fill();

    ctx.fillStyle =
        "white";

    ctx.fillText(
        "PROMPT",
        centerX-20,
        centerY+5
    );

    scores.forEach(
        (item,index)=>{

        const angle =
            (
                index/
                scores.length
            )*
            Math.PI*2;

        const distance =
            100 +
            (
                1-item.score
            )*200;

        const x =
            centerX +
            Math.cos(angle)*
            distance;

        const y =
            centerY +
            Math.sin(angle)*
            distance;

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
            "white";

        ctx.stroke();

        ctx.beginPath();

        ctx.arc(
            x,
            y,
            20,
            0,
            Math.PI*2
        );

        ctx.fillStyle =
            "#10b981";

        ctx.fill();

        ctx.fillStyle =
            "white";

        ctx.fillText(
            item.model,
            x-20,
            y+35
        );
    });
}