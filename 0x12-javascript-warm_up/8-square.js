#!/usr/bin/node
const arg = process.argv;
if (isNaN(arg[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg[2]; i++) {
    console.log('X'.repeat(arg[2]));
  }
}
