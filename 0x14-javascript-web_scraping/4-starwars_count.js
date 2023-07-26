#!/usr/bin/node
/**
 * Prints the number of movies where,
 * the character “Wedge Antilles” is present
 */
const args = process.argv.slice(2);

if (args.length === 1) {
  const request = require('request');
  const url = args[0];
  let filmNum = 0;
  request(url, function (error, _, body) {
    if (error) {
      console.error(error);
    }
    const data = JSON.parse(body);
    for (const film of data.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          filmNum++;
        }
      }
    }
    console.log(filmNum);
  });
} else {
  console.log('Usage: ./4-starwars_count.js URL');
}
