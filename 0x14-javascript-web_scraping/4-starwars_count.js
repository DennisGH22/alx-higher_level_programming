#!/usr/bin/node
const request = require('request');

function countMoviesWithCharacter (apiUrl, characterId) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const films = JSON.parse(body).results;
      const moviesWithWedge = films.filter((film) => {
        return film.characters.includes(`https://swapi-api.alx-tools.com/api/films/${characterId}/`);
      });
      console.log(moviesWithWedge.length);
    }
  });
}

const [,, apiUrl] = process.argv;
countMoviesWithCharacter(apiUrl, 18);
