var dataset = [5,10,13,19,21,25,22,18,15,13,11,12,15,20,18,17,16,18,23,25];
var dataset1 = [5,10,13,19,21,25];

var dataValida = dataset;

console.log(dataset.length);

var w = 500;
var h = 100;
var barPadding = 1;

var svgv = d3.select("body")
				.append("svg")
				.attr("width",w)
				.attr("height",h);

svgv.selectAll("rect")
	.data(dataset)
	.enter()
	.append("rect")
			
	.attr("x",function(dato,indice){
		return indice * (w / dataValida.length);
	})
	.attr("y",function(dato){
		return h - dato * 3;
	})
	.attr("width",w / dataValida.length - barPadding)
	.attr("height",function(dato){
		return dato * 3;
	})
	.style("fill", function(dato, indice){
		return "rgb(0, 0, " + (dato * 10) + ")"
	})
	
d3.select("svg").selectAll("text")
	.data(dataset)
	.enter()
	.append("text")
	.attr("x", function(dato, indice){
		return indice * (w / dataValida.length) + (w / dataValida.length - barPadding) * 0.5
	})
	.attr("y", function(dato){
		return h - (dato * 3) + 15
	})
	.text(function(dato){
		return dato
	})
	.style("text-anchor", "middle")
	.style("fill", "white")