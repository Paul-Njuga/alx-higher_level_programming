#!/usr/bin/node
/* Reads and prints the contents of a file */
const args = process.argv.slice(2);

if (args.length === 1) {
  const fs = require('fs');
  const filePath = args[0];

  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}
