#!/usr/bin/node
function fact (i) {
  if (isNaN(i)) {
    return 1;
  }
  if (i === 0 || i === 1) {
    return 1;
  }
  return i * fact(i - 1);
}

const num = parseInt(process.argv[2]);
const factorial = fact(num);
console.log(factorial);
