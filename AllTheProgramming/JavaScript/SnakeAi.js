class apple {
	gencord() {
		this.pos = [Math.floor(Math.random() * (sizer[0] / 20)), Math.floor(Math.random() * (sizer[1] / 20))];
		for (let j in player.body) {
			if (this.pos[0] == player.body[j][0] && this.pos[1] == player.body[j][1]) {
				this.gencord();
			}
		}
	}
	constructor() {
		this.gencord()
		fill(255, 0, 0)
		rect(this.pos[0] * 20, this.pos[1] * 20, 20)
	}
}


class snake {
	constructor(x, y, length) {
		this.x = x;
		this.y = y;
		this.body = [];
		this.queue = [];
		this.direction = 1;
		this.tick = 0;
		this.dead = false;
		this.eat = false;
		this.deathIsSoon = false;
		this.pathfind = [];
		for (let k = 1; k <= length; k++) {
			this.body.push([this.x - k, this.y])
		}
	}
	ai(panic = false) {
		let output;
		if (!panic) {
			output = astar(sizer[0] / 20, sizer[1] / 20, [this.x, this.y], appa.pos, this.body)
		} else {
			output = astar(sizer[0] / 20, sizer[1] / 20, [this.x, this.y], [this.body.length - 1[0], this.body.length - 1[1]], this.body, true, true)
		}
		if (output == null) {
			this.deathIsSoon = true;
			return false;
		} else {
			this.deathIsSoon = false;
			this.pathfind = output;
			let final = [];
			for (let a = 0; a < output.length - 1; a++) {
				if (output[a][0] - output[a + 1][0] == 1) {
					final.unshift(1)
				} else if (output[a][1] - output[a + 1][1] == 1) {
					final.unshift(2)
				} else if (output[a][0] - output[a + 1][0] == -1) {
					final.unshift(3)
				} else if (output[a][1] - output[a + 1][1] == -1) {
					final.unshift(4)
				}
			}
			player.queue = final;
			return true;
		}

	}
	move() {
		this.tick++;
		if (this.tick > 5) {
			this.tick = 0;
			this.body.unshift([this.x, this.y]);
			if (this.eat == false) {
				this.body.pop();
			} else {
				this.eat = false;
			}
			if (this.queue.length > 0) {
				this.direction = this.queue[0];
			}
			if (this.deathIsSoon) {
				this.direction = 1;
			}
			this.queue.shift();
			switch (this.direction) {
				case 1:
					this.x++;
					break;
				case 2:
					this.y++;
					break;
				case 3:
					this.x--;
					break;
				case 4:
					this.y--;
					break;
			}

		}
		fill(255, 0, 0)
		rect(appa.pos[0] * 20, appa.pos[1] * 20, 20, 20)
		if (this.x == appa.pos[0] && this.y == appa.pos[1]) {
			this.eat = true;
			appa = new apple();
			this.ai();
		}
		fill(50, 205, 50)
		if (this.deathIsSoon) {
			fill(205, 13, 13);
			let lets_try = this.ai();
			if (!lets_try) {
				let come_on = this.ai(true);
				if (!come_on) {
					console.warm('the end is near')
				}
			}

		}
		rect(this.x * 20, this.y * 20, 20, 20)
		for (let g = 0; g < this.body.length; g++) {
			rect(this.body[g][0] * 20, this.body[g][1] * 20, 20, 20)
			if (this.x == this.body[g][0] && this.y == this.body[g][1] || this.x > width / 20 || this.y > height / 20 || this.x < 0 || this.y < 0) {
				this.dead = true;
			}
		}
		for (let y in this.pathfind) {
			fill(0, 0, 255, 10)
			rect(this.pathfind[y][0] * 20, this.pathfind[y][1] * 20, 20, 20)
		}
	}
}


var sizer = [];

function setup() {
	createCanvas(180, 180);
	background(100);
	sizer = [width, height]
	appa = new apple();
	player.ai();
}
var player = new snake(3, 3, 3);
var appa;

function draw() {
	stroke(0)
	background(255, 255, 255, 100);
	player.move()
	stroke(100)
	for (let i = 0; i < width / 20; i++) {
		line(i * 20, 0, i * 20, height)
	}
	for (let j = 0; j < height / 20; j++) {
		line(0, j * 20, width, j * 20)
	}
}

function astar(gridX, gridY, start, end, body, long = false, deathIsSoon = false) {
	let percentage = [];
	let openSet = [];
	let closedSet = [];
	let path = [];

	function heu(a, b) {
		let d = dist(a.x, a.y, b.x, b.y)
		return d;
	}
	class node {
		constructor(x, y) {
			this.x = x;
			this.y = y;
			this.f = 0;
			this.g = 0;
			this.h = 0;
			this.Nei = [];
			this.wall = false;
			for (let ii = 0; ii < body.length; ii++) {
				if (body[ii][0] == this.x && body[ii][1] == this.y) {
					this.wall = true
				}
			}

		}
		findNei() {
			let n = [];
			if (this.x < gridX - 1) {
				n.push(grid[this.x + 1][this.y])
			}
			if (this.x > 0) {
				n.push(grid[this.x - 1][this.y])
			}
			if (this.y < gridY - 1) {
				n.push(grid[this.x][this.y + 1])
			}
			if (this.y > 0) {
				n.push(grid[this.x][this.y - 1])
			}
			return n;
		}
	}
	//create grid
	let grid = [];
	for (let j = 0; j < gridX; j++) {
		let colum = [];
		for (let i = 0; i < gridY; i++) {
			colum.push(new node(j, i))
		}
		grid.push(colum)
	}
	openSet.push(grid[start[0]][start[1]])
	end = grid[end[0]][end[1]]
	for (let k = 0; k < grid.length; k++) {
		for (let kk = 0; kk < grid[k].length; kk++) {
			grid[k][kk].Nei = grid[k][kk].findNei();
		}
	}
	while (openSet.length > 0) {
		let current;
		let lowest = 0;
		for (let j = 0; j < openSet.length; j++) {
			if (!long) {
				if (openSet[j].f < openSet[lowest].f) {
					lowest = j;
				}
			} else {
				if (openSet[j].f > openSet[lowest].f) {
					lowest = j;
				}
			}
		}
		current = openSet[lowest];
		if (openSet[lowest] == end) {
			//console.log('done')
			let temp = current;
			path.push(temp)
			while (temp.previous) {
				path.push(temp.previous)
				temp = temp.previous;
			}
			//console.log(path)
			let path2 = [];
			for (let g = 0; g < path.length; g++) {
				path2.push([path[g].x, path[g].y])
			}
			//console.log(percentage)
			return path2;
		}
		openSet.splice(openSet.indexOf(current), 1)
		closedSet.push(current)
		let neighbors = current.Nei;
		for (let i = 0; i < neighbors.length; i++) {
			let neighbor = neighbors[i];
			let path2get = [];
			let temp = current;
			let counting = 0;
			while (temp.previous) {
				path2get.push([temp.x, temp.y])
				temp = temp.previous;
				counting++;
			}
			for (let be = 0; be < body.length - counting; be++) {
				path2get.push(body[be])
			}
			let reachable = floodFill(path2get, [neighbor.x, neighbor.y], [gridX, gridY]);
			let percent = reachable / (gridX * gridY - body.length)
			percent *= 100;
			//percentage.push('reachable: ' + reachable + ' size: ' + (gridX * gridY - body.length));
			if (!closedSet.includes(neighbor) && neighbor.wall == false && percent > 80 || !closedSet.includes(neighbor) && neighbor.wall == false && deathIsSoon == true) {
				let tempg = current.g + 1;
				if (openSet.includes(neighbor)) {
					if (!long) {
						if (tempg < neighbor.g) {
							neighbor.g = tempg;
						}
					} else {
						if (tempg > neighbor.g) {
							neighbor.g = tempg;
						}
					}
				} else {
					neighbor.g = tempg;
					openSet.push(neighbor)
				}
				neighbor.h = heu(neighbor, end)
				neighbor.f = neighbor.g + neighbor.h
				neighbor.previous = current;
			} else {

				if (neighbor.wall == true && percent > 80 || neighbor.wall == true && deathIsSoon == true) {
					let temp = current;
					let count = 0;
					while (temp.previous) {
						count++
						temp = temp.previous;
					}
					//console.log(count)
					if (count > body.length && !closedSet.includes(neighbor)) {
						//console.log('cutting')
						let tempg = current.g + 1;
						if (openSet.includes(neighbor)) {
							if (!long) {
								if (tempg < neighbor.g) {
									neighbor.g = tempg;
								}
							} else {
								if (tempg < neighbor.g) {
									neighbor.g = tempg;
								}
							}
						} else {
							neighbor.g = tempg;
							openSet.push(neighbor)
						}
						neighbor.h = heu(neighbor, end)
						neighbor.f = neighbor.g + neighbor.h
						neighbor.previous = current;
					}
				}
			}
		}
	}
	if(!long && deathIsSoon == false) {
		//console.log('trying again')
		let attempt2 = astar(sizer[0] / 20, sizer[1] / 20, [player.x, player.y], appa.pos, player.body,true)
		return attempt2;
	}
	else if(long == true && deathIsSoon == false) {
		//console.log('trying once more')
		let attempt2 = astar(sizer[0] / 20, sizer[1] / 20, [player.x, player.y], appa.pos, player.body,false,true)
		return attempt2;
	}
	else {
		console.log('oh no...')
		return null;
	}
}
function floodFill(walls,point,size) {
	let q = [];
	let done = [];
	class space {
		constructor(x,y) {
			this.x = x;
			this.y = y;
			this.wall = false;
			this.neighbors = [];
			for(let k in walls) {
				if(this.x == walls[k][0] && this.y == walls[k][1]) {
					this.wall = true;
				}
			}
		}
		find() {
			let nn = [];
			if (this.x < size[0] - 1) {
				nn.push(gridd[this.x + 1][this.y])
			}
			if (this.x > 0) {
				nn.push(gridd[this.x - 1][this.y])
			}
			if (this.y < size[1] - 1) {
				nn.push(gridd[this.x][this.y + 1])
			}
			if (this.y > 0) {
				nn.push(gridd[this.x][this.y - 1])
			}
			this.neighbors = nn;
		}
	}
	let gridd = [];
	let col = [];
	for(let i = 0; i < size[0]; i++) {
		col = [];
		for(let j = 0; j < size[1]; j++) {
			col.push(new space(i,j))
		}
		gridd.push(col)
	}
	for(let k in gridd) {
		for(let kk in gridd[k]) {
			gridd[k][kk].find();
		}
	}
	q.push(gridd[point[0]][point[1]]);
	while(q.length > 0) {
		let currentt = q[0];
		q.shift();
		done.push(currentt);
		//console.log(current.neighbors.length)
		for(let k = 0 ; k < currentt.neighbors.length; k++) {
			if(currentt.neighbors[k].wall == false && !done.includes(currentt.neighbors[k]) && !q.includes(currentt.neighbors[k])) {
				q.push(currentt.neighbors[k]);
			}
		}
	}
	return done.length;
}s