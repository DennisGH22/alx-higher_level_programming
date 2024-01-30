#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function fetchAndSaveWebpage (url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (writeError) => {
        if (writeError) {
          console.error(`Error writing to file: ${writeError.message}`);
        } else {

        }
      });
    }
  });
}

const [,, url, filePath] = process.argv;
fetchAndSaveWebpage(url, filePath);
