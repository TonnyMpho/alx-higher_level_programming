#!/usr/bin/node
// script that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body);

    const count = movies.results.reduce((i, movie) => {
      if (movie.characters.includes(character)) {
        return i + 1;
      }
	return i;
    }, 0);
    console.log(count);
  }
});
