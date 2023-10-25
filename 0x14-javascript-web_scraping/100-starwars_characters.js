#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body);
    data.characters.forEach(characterUrl => {
      request(characterUrl, (err, res, body) => {
        if (err) console.log(err);
        const character = JSON.parse(body);
        console.log(character.name);
      });
    });
  }
});
