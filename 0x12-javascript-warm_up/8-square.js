#!/usr/bin/node
const args = process.argv.slice(2);
const firstArgument = parseInt(args[0], 10);

if (!isNaN(firstArgument)) {
  for (let i = 0; i < firstArgument; i++) {
	let square = '';
	for (let j = 0; j < firstArgument; j++) {
    	square += 'X';
	}
	console.log(square);
  }
} else {
  console.log('Missing size');
}
