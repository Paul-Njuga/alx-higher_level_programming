#!/usr/bin/node
const args = process.argv;

function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  console.log(sum);
}
add(args[2], args[3]);
