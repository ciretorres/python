
var margin = {top: 100, bottom: 100, left: 100, right: 100};
var width = 700 - margin.left - margin.right;
var height = 700 - margin.top - margin.bottom;


var dataset = [ //----------------------- Making a dictionary with indexes
				{x:5, y:20, radio:4},
				{x:480, y:90, radio:7},
				{x:250, y:50, radio:12},
				{x:100, y:33, radio:4},
				{x:330, y:95, radio:23},
				{x:410, y:12, radio:19},
				{x:475, y:44, radio:56},
				{x:25, y:67, radio:76},
				{x:85, y:21, radio:29},
				{x:220,y:88, radio:3}
];


//-------------------------------- Getting the max values from x, y, radio
var maxx = d3.max(dataset,function(d){return d.x});
var maxy = d3.max(dataset,function(d){return d.y});
var maxr = d3.max(dataset,function(d){return d.radio});

// var limx = 500;
// var limy = 500;

var escalax = d3.scale.linear().domain([0,maxx]).range([0,width]);
var escalay = d3.scale.linear().domain([0,maxy]).range([height,0]);
var escalar = d3.scale.linear().domain([0,maxr]).range([0,20]);

var xEje = d3.svg.axis().scale(escalax).orient("bottom");
var yEje = d3.svg.axis().scale(escalay).orient("left");

var svgv = d3.select("body").append("svg")
	//.attr("width", "500")
	.attr("width",width + margin.left + margin.right)
	//.attr("height", "200")
	.attr("height",height + margin.top + margin.bottom)
	.append("g")
	.attr("transform","translate(" + margin.left + "," + margin.top + ")");

svgv.append("g")
	.attr("class","eje")
	.attr("transform","translate(" + escalax(0) + "," + escalay(0) +")")
	.call(xEje);

svgv.append("g")
	.attr("class","eje")
	.attr("transform","translate(" + escalax(0) + "," + escalay(maxy) +")")
	.call(yEje);

svgv.selectAll(".circulo")
	.data(dataset)
	.enter() // Como la clase no existe lo manda al enter y le pido que me mande lo que hay en el enter
	.append("circle")
	.attr("class","circulo")
	.attr("cx",function(dato){
		return escalax(dato["x"]);
	})
	.attr("cy",function(dato){
		return escalay(dato["y"]);
	})
	.attr("r",function(dato){
		return escalar(dato["radio"]);
	})
	.style("opacity",0.3)
	.style("stroke","black")
	.style("stroke-width",1);

svgv.selectAll(".etiquetas")
	.data(dataset)
	.enter()
	.append("text")
	.attr("x",function(dato){return escalax(dato["x"])})
	.attr("y",function(dato){return escalay(dato.y)})
	.text(function(dato){return "(" + dato["x"] + "," + dato["y"] +")"});