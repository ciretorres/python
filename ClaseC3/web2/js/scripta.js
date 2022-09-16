var circle = d3.selectAll("circle");
circle.style("fill", "blue");
circle.attr("r", 30);

d3.select("svg").append("circle")
    .attr("cx", 60)
    .attr("cy", 80)
    .attr("r", 10);