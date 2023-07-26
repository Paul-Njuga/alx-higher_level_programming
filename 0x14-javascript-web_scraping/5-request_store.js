#!/usr/bin/node
/**
 * Prints the number of movies where,
 * the character “Wedge Antilles” is present
 */
const args = process.argv.slice(2);

if (args.length === 2) {
  const url = args[0];
  const filePath = args[1];
  const request = require('request');
  const fs = require('fs');

  request(url, function (error, _, body) {
    if (error) {
      process.exit(1);
    }
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        process.exit(1);
      }
    });
  });
} else {
  console.log('Usage: ./5-request_store.js URL filePath');
}
