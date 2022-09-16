var o = d3.scale.ordinal()
	//.domain([1, 2, 3, 4])
	.domain(["Enero", "Febrero", "Marzo", "Abril"])
	.rangePoints([0, 100]);

//console.log(o(3))
//console.log(o("Febrero"))

var svg = d3.select("body").append("svg")
	.attr("width", 1000)
	.attr("height", 1000)
	.append("g");
	
//d3.json()
d3.csv("./datos/sent.csv", function(error, datos_sin){

	var datos_fil = datos_sin.filter(function(d,i){
		return d.Procesados != 0;
	});

	//var datos = datos_sin.sort(function(a,b){
	var datos = datos_fil.sort(function(a,b){
		//return a.Procesados - b.Procesados;
		return -1 * (a.Procesados - b.Procesados);
	});
	//console.log(datos);
	//console.log(error);
	var rangox =  d3.extent(datos, function(d,i){ // Obtain an array from min to max
		//console.log(d, d.Sentenciados);
		return parseInt(d.Sentenciados);
	});
	var rangoy = d3.extent(datos, function(d,i){
		return parseInt(d.Procesados);
	});

	var estados = datos.map(function(d){return d.Estado}); // Recorre el index de estados y guarda cada valor en una lista
	//var estados_ord = estados.sort();
	//console.log(estados);
	//console.log(rangox);
	//console.log(rangoy);
	var scalex = d3.scale.linear().domain(rangox).range([100, 900]);
	var scaley = d3.scale.linear().domain(rangoy).range([400, 100]);
	
	var scalex2 = d3.scale.ordinal().domain(estados).rangeBands([0, 1000], 0.1);
	//var scalex2 = d3.scale.ordinal().domain(estados_estados_ord).rangeBands([0, 1000], 0.1);

	//console.log(scalex2("OAXACA"));
	//console.log(scalex2("PUEBLA"));

	svg.selectAll(".circulo").data(datos)
		.enter()
		.append("circle") //------------------------------------- Círculos
		.attr("class", "circulo")
		.attr("cx", function(d,i){return scalex2(d.Estado)})
		.attr("cy", function(d,i){return scaley(d.Procesados)})
		.attr("r", 2);

	svg.selectAll(".barras").data(datos)
		.enter()
		.append("rect") //--------------------------------------- Rectángulos
		.attr("class", "barras")
		.attr("x", function(d,i){return scalex2(d.Estado)})
		.attr("y", function(d,i){return scaley(d.Procesados)})
		.attr("height", function(d,i){return scaley(0) - scaley(d.Procesados)})
		.attr("width", scalex2.rangeBand())
		.style("cursor", "pointer")
		.on("mouseover", function(d,i){
			//console.log(d);
			d3.select(this).style("fill", "blue");
			
			svg.append("text")
				.attr("class", "legenda")
				.attr("x", 100)
				.attr("y", 100)
				.text("Personas procesadas " + d.Procesados)
				.style("font-size", "40px");
		})
		.on("mouseout", function(d,i){
			d3.select(this).style("fill", "black");
			d3.select(".legenda").remove();
				//.text("Personas procesadas ");
		})
	
})
