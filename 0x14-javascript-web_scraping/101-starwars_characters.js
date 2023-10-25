#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getCharacters (characters, idx) {
  const characterUrl = characters[idx];

  request(characterUrl, (err, res, body) => {
    if (err) console.log(err);
    const character = JSON.parse(body);
    console.log(character.name);

    idx++;
    if (idx < characters.length) {
      getCharacters(characters, idx);
    }
  });
}

request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body);
    const characters = data.characters;

    if (characters) {
      getCharacters(characters, 0);
    }
  }
});
