#!/usr/bin/node
const request = require('request');

function printCharactersInMovie (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const characters = body.characters;

      characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error(`Error fetching character: ${characterError.message}`);
          } else if (characterResponse.statusCode !== 200) {
            console.error(`Request failed with status code: ${characterResponse.statusCode}`);
          } else {
            console.log(characterBody.name);
          }
        });
      });
    }
  });
}

const [,, movieId] = process.argv;
printCharactersInMovie(movieId);
