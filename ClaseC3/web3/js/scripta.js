var svgv = d3.select("body").append("svg");

var w = 500;
var h = 100;

svgv.attr("width",w)
	.attr("height",h);

var dataset = [5, 10, 15, 20, 25];
var dataset1 = [7,14,21,28];

var circulos = svgv.selectAll("circle")
	.data(dataset)
	.enter()
	.append("circle");

circulos.attr("cx", function(dato, indice){
		return (indice * 50) + 25
	})
	.attr("cy", h/2)
	.attr("r", function(dato){
		return dato
	})
	.style("fill", "yellow")
	.style("stroke", "orange")
	.style("stroke-width", function(dato){
		return dato * 0.5
	});


