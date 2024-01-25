#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  fs.promises.writeFile(filePath, content, 'utf-8')
    .then(() => {

    })
    .catch(error => {
      console.error(`An error occurred while writing to ${filePath}: ${error.message}`);
    });
}

const [,, filePath, content] = process.argv;
writeToFile(filePath, content);
