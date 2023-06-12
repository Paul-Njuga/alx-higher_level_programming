#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
