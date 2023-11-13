#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (n) {
  n = parseInt(n);
  if (!isNaN(n)) {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      let result = 1;
      for (let i = 2; i <= args[0]; i++) {
        result *= i;
      }
      return result;
    }
  }
}
console.log(factorial(args[0]));
