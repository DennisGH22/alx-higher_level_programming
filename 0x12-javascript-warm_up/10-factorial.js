#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0 || args.length < 1) {
  console.log('1');
} else {
  let result = 1;
  for (let i = 2; i <= args[0]; i++) {
    result *= i;
  }
  console.log(result);
}
