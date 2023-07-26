#!/usr/bin/node
/**
 * Prints the number of movies where,
 * the character “Wedge Antilles” is present
 */
const args = process.argv.slice(2);

if (args.length === 1) {
  const url = args[0];
  let filmNum = 0;
  const char = 'http://swapi.co/api/people/18/';
  const request = require('request');
  request(url, function (error, _, body) {
    if (error) {
      process.exit(1);
    }
    const data = JSON.parse(body);
    for (const film of data.results) {
      if (film.characters.includes(char)) {
        filmNum++;
      }
    }
    console.log(filmNum);
  });
} else {
  console.log('Usage: ./4-starwars_count.js URL');
}
