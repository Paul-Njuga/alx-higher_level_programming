#!/usr/bin/node
const args = process.argv.slice(2);

/* Process.execPath & path to js file */
if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
