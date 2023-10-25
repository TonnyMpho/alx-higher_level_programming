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
    let count = 0;

    movies.results.forEach(movie => {
      if (movie.characters.includes(character)) {
        count++;
      }
    });
    console.log(count);
  }
});
