function renderGraph(graph) {

    const canvas =
        document.getElementById(
            "graphCanvas"
        );

    const ctx =
        canvas.getContext("2d");

    canvas.width =
        canvas.parentElement.clientWidth - 40;

    canvas.height = 350;

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    ctx.fillStyle = "white";
    ctx.font = "18px Arial";

    ctx.fillText(
        "Model Comparison",
        20,
        30
    );

    graph.forEach(
        (item, index) => {

            const y =
                70 +
                index * 70;

            const barWidth =
                item.percentage * 5;

            ctx.fillStyle =
                "#2563eb";

            ctx.fillRect(
                150,
                y,
                barWidth,
                35
            );

            ctx.fillStyle =
                "white";

            ctx.fillText(
                item.model,
                20,
                y + 23
            );

            ctx.fillText(
                item.percentage + "%",
                160 + barWidth,
                y + 23
            );
        }
    );
}