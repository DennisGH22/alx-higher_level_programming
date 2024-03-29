#!/usr/bin/node
const request = require('request');

function printCharactersInMovie (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      characterUrls.forEach(characterUrl => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error(`Error fetching character: ${characterError.message}`);
          } else if (characterResponse.statusCode !== 200) {
            console.error(`Request failed with status code: ${characterResponse.statusCode}`);
          } else {
            const character = JSON.parse(characterBody);
            console.log(character.name);
          }
        });
      });
    }
  });
}

const [,, movieId] = process.argv;
printCharactersInMovie(movieId);
