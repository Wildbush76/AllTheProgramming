function setup() {
	createCanvas(1200,500);
	background(100);
}
var size = 400;
function thing(radius) {
	let div = Math.ceil(2*Math.PI*radius);
	div = 360/div;
	let final = [];
	for(let k = 0; k < 360; k+=div) {
		let x = Math.cos(k * (Math.PI/180)) * radius + mouseX;
		let y = Math.sin(k * (Math.PI/180)) * radius + mouseY;
		let total = Math.floor(x/20) + Math.floor(y/20)*width/20;
		if(!final.includes(total))
		{
			final.push(total);
		}
	}
	return final;
}
function draw() {
	background(255,255,255);
	//draw grid
	stroke(0);
	strokeWeight(1);
	for(let x = 0; x < width; x+=20) {
		line(x,0,x,height);
	}
	for(let y = 0; y < height; y+=20) {
		line(0,y,width,y)
	}
	let pos = thing(size/2);
	fill(0,255,0)
	//console.log(pos)
	for(let j in pos) {
		rect((pos[j]%(width/20))*20,20 * Math.floor(pos[j]/(width/20)),20,20)
	}
	noFill();
	stroke(0,0,255);
	strokeWeight(3);
	ellipse(mouseX,mouseY,size);
}