#!/usr/bin/node
const args = process.argv.slice(2);
const a = parseInt(args[0], 10);
const b = parseInt(args[1], 10);

function add(a, b) {
	console.log(a + b);
}
add (a, b);
