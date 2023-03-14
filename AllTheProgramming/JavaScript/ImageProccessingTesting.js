var imag;
var o;
var video;
var dithering = true;//wether dithering is used or not 

function preload() {
	//imag = loadImage('charlottle.jpg');
	imag = createCapture(VIDEO);
  imag.size(512, 512);
	imag.hide();
	// ^ link for the image you want to use

}

function setup() {
	createCanvas(imag.width, imag.height);
	background(100);
}
var scal = [128, 128];
var num = 1;

function draw() {

	//image(o, 0, 0)
	image(imag, 0, 0);
	imag.loadPixels();
	//filter(GRAY);
	for (let y = 0; y < imag.height - 1; y++) {
		for (let x = 1; x < imag.width - 1; x++) {
			let index = x + y * imag.width;
			index *= 4;
			let r = imag.pixels[index];
			let g = imag.pixels[index + 1];
			let b = imag.pixels[index + 2];
			r = Math.round((r / 255) * num) * (255 / num);
			g = Math.round((g / 255) * num) * (255 / num);
			b = Math.round((b / 255) * num) * (255 / num);
			let error_R = imag.pixels[index] - r;
			let error_G = imag.pixels[index + 1] - g;
			let error_B = imag.pixels[index + 2] - b;
			if (dithering) {
				imag.pixels[index + 4] = imag.pixels[index + 4] + error_R * 7 / 16;
				imag.pixels[(index + 4) + 1] = imag.pixels[(index + 4) + 1] + error_G * 7 / 16;
				imag.pixels[(index + 4) + 2] = imag.pixels[(index + 4) + 2] + error_B * 7 / 16;
				imag.pixels[index + imag.width * 4 - 4] = imag.pixels[index + imag.width * 4 - 4] + error_R * 3 / 16;
				imag.pixels[(index + imag.width * 4 - 4) + 1] = imag.pixels[(index + imag.width * 4 - 4) + 1] + error_G * 3 / 16;
				imag.pixels[(index + imag.width * 4 - 4) + 2] = imag.pixels[(index + imag.width * 4 - 4) + 2] + error_B * 3 / 16;
				imag.pixels[index + imag.width * 4] = imag.pixels[index + imag.width * 4] + error_R * 5 / 16;
				imag.pixels[(index + imag.width * 4) + 1] = imag.pixels[(index + imag.width * 4) + 1] + error_G * 5 / 16;
				imag.pixels[(index + imag.width * 4) + 2] = imag.pixels[(index + imag.width * 4) + 2] + error_B * 5 / 16;
				imag.pixels[index + 4 + imag.width * 4] = imag.pixels[index + 4 + imag.width * 4] + error_R * 1 / 16;
				imag.pixels[(index + 4 + imag.width * 4) + 1] = imag.pixels[(index + 4 + imag.width * 4) + 1] + error_G * 1 / 16;
				imag.pixels[(index + 4 + imag.width * 4) + 2] = imag.pixels[(index + 4 + imag.width * 4) + 2] + error_B * 1 / 16;
			}
			imag.pixels[index] = r;
			imag.pixels[index + 1] = g;
			imag.pixels[index + 2] = b;
			imag.pixels[index + 3] = 255;
		}
	}
	imag.updatePixels();
}