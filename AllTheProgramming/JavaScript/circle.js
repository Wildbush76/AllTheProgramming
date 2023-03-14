function setup() {
	createCanvas(windowWidth, windowHeight);
	background(100);
	for(var xx = 0;xx < r.length;xx++)
	{
	i.push(Math.floor((Math.random() * 150) + 1));
		fall.push(0)
		rr.push(Math.floor((Math.random() * 255) + 1));//adds the first red values
		gg.push(Math.floor((Math.random() * 255) + 1));//adds the first green values 
		bb.push(Math.floor((Math.random() * 255) + 1));//adds the first blue values
		
	}
}
var rr = [];
var gg = [];
var bb = [];
var radius = 255;
var gravity = 0.01;
var fall = [];
var r = [255];
var i = [];//it some how works
var thing = 100;
function draw() {
	//fill(255,0,0)
	noStroke();
	background(0,0,0,25)
	if(Math.floor((Math.random() * 5) + 1) == 3)
	{
	//r.push(radius)
		r.push(Math.floor((Math.random() * 300) + 200));//randomize the radius
		i.push(Math.floor((Math.random() * 150) + 1));//adds where it is on circle
		fall.push(0);//adds the gravity value
		rr.push(Math.floor((Math.random() * 255) + 1));//randomizes red value
		gg.push(Math.floor((Math.random() * 255) + 1));//randomizes green value
		bb.push(Math.floor((Math.random() * 255) + 1));//randomizes blue value
	}
	for(var xxx = 0;xxx < r.length;xxx++)
	{
	 var x = windowWidth/2 + r[xxx] * Math.cos(2 * Math.PI * i[xxx] / thing); //get circle X
    var y = windowHeight/2 + r[xxx] * Math.sin(2 * Math.PI * i[xxx] / thing); //gets circle Y
		fill(rr[xxx],gg[xxx],bb[xxx])
	rect(x,y,10,10)//the cubes
		i[xxx]++;
		r[xxx]-=fall[xxx];
		fall[xxx]+=gravity
		if(r[xxx] < 0)
		{
		r.splice(xxx,1);
			i.splice(xxx,1);
       fall.splice(xxx,1);	
		}
	}
	fill(255)
	ellipse(windowWidth/2,windowHeight/2,10,10)//center circle
	//the blackhole thingy^^^^^^^^^^^^^^^
}
