function renderGraph(graph){

    const canvas =
    document.getElementById(
        "graphCanvas"
    );

    const ctx =
    canvas.getContext("2d");

    canvas.width =
    canvas.parentElement
    .clientWidth;

    canvas.height = 300;

    ctx.clearRect(

        0,
        0,
        canvas.width,
        canvas.height

    );

    const barWidth = 80;

    const spacing = 120;

    graph.forEach(

        (item,index)=>{

        const x =
        60 +
        index*spacing;

        const height =
        item.percentage * 2;

        const y =
        250-height;

        ctx.fillStyle =
        "#2563eb";

        ctx.fillRect(

            x,
            y,
            barWidth,
            height

        );

        ctx.fillStyle =
        "white";

        ctx.fillText(

            item.model,

            x,

            270

        );

        ctx.fillText(

            item.percentage
            +"%",

            x,

            y-10

        );

    });

}