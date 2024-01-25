#!/usr/bin/node
const request = require('request');

function displayStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

const [,, url] = process.argv;
displayStatusCode(url);
