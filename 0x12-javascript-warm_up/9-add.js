#!/usr/bin/node
function add (a, b) {
  const sum = Number(a) + Number(b);
  console.log(sum);
}

add(process.argv[2], process.argv[3]);
