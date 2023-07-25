#!/usr/bin/node
/* Displays the status code of a GET request */
const args = process.argv.slice(2);

if (args.length === 1) {
  const url = args[0];
  const request = require('request');
  request(url, function (error, response) {
    console.log('code:', response.statusCode);
  });
} else {
  console.log('Usage: ./2-statuscode.js URL');
}
