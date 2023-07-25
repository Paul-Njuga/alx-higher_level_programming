#!/usr/bin/node
/* Reads and prints the contents of a file */
const args = process.argv.slice(2);

if (args.length === 2) {
  const fs = require('fs');
  const filePath = args[0];
  const dt = args[1];

  fs.writeFile(filePath, dt, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log(dt);
    }
  });
}
