function setup() {
	createCanvas(windowWidth, windowHeight);
	background(100);
	me = new player(windowWidth / 2, windowHeight / 2, 5)
}
class player {
	constructor(x, y, laser) {
		this.pos = { 'x': x, 'y': y }
		this.b = laser
	}
	render() {
		fill(173, 216, 230)
		ellipse(this.pos.x, this.pos.y, 40)
	}

	shoot(startX, startY, targetX, targetY, left) {
		if (left < 0) {
			return
		}
		strokeWeight(2)
		let slope = (targetY - startY) / (targetX - startX)
		let intercept = targetY - (targetX * slope)
		let lefx = 0
		if (targetX - startX > 0) {
			lefx = windowWidth
		}
		var yinter = (lefx * slope) + intercept
		let lefy = 0
		if (targetY - startY > 0) {
			lefy = windowHeight
		}
		var xinter = (lefy - intercept) / slope
		stroke(255, 0, 0)
		if (yinter > 0 && yinter < windowHeight) {
			line(startX, startY, lefx, yinter)
			let ry = (-(startY - yinter)) + yinter
			this.shoot(lefx, yinter, startX, ry, left - 1)
			//ellipse(lefx,yinter,20)
		}
		else {
			line(startX, startY, xinter, lefy)
			let rx = (-(startX - xinter)) + xinter
			this.shoot(xinter, lefy, rx, startY, left - 1)
			//ellipse(xinter,lefy,20)
		}
	}
}
var me
var keys = []
keyPressed = function () {
	keys[keyCode] = true;
}
keyReleased = function () {
	keys[keyCode] = false;
}
function draw() {
	background(255)
	if (keys[87]) {
		me.pos.y -= 5
	}
	else if (keys[83]) {
		me.pos.y += 5
	}
	if (keys[65]) {
		me.pos.x -= 5
	}
	else if (keys[68]) {
		me.pos.x += 5
	}
	me.render()
	me.shoot(me.pos.x, me.pos.y, mouseX, mouseY, 40)
	stroke(0)
	strokeWeight(2)
}