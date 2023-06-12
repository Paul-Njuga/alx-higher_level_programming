#!/usr/bin/node
const args = process.argv;

/* Process.execPath & path to js file */
if (!args[2]) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
