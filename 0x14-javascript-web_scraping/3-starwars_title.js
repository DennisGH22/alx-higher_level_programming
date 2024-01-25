#!/usr/bin/node
const request = require('request');

function getStarWarsMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const movie = JSON.parse(body);
      console.log(`Title of Star Wars Episode ${movie.episode_id}: ${movie.title}`);
    }
  });
}

const [,, movieId] = process.argv;
getStarWarsMovieTitle(movieId);
