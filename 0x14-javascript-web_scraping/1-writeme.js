#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  fs.promises.writeFile(filePath, content, 'utf-8')
    .then(() => {
      console.log(`Content has been successfully written to ${filePath}`);
    })
    .catch(error => {
      console.error(`An error occurred while writing to ${filePath}: ${error.message}`);
    });
}

const [,, filePath, content] = process.argv;
writeToFile(filePath, content);
