#!/usr/bin/node
/**
 * Prints the title of a Star Wars movie,
 * where the episode number matches a given integer
 */
const args = process.argv.slice(2);

if (args.length === 1) {
  const request = require('request');
  const endPoint = 'https://swapi-api.alx-tools.com/api/films/';
  const id = args[0];
  const folder = '/';
  const url = endPoint.concat(id, folder);
  request(url, function (error, _, body) {
    if (error) {
      process.exit(1);
    }
    const data = JSON.parse(body);
    if (data.url === url) {
      console.log(data.title);
    }
  });
} else {
  console.log('Usage: ./3-starwars_title.js ID');
}
