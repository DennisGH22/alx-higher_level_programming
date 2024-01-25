#!/usr/bin/node
const fs = require('fs');

function readAndPrintFile (filePath) {
  fs.promises.readFile(filePath, 'utf-8')
    .then((data) => {
      console.log(data);
    })
    .catch((err) => {
      console.error(`An error occurred: ${err}`);
    });
}

const filePath = process.argv[2];
readAndPrintFile(filePath);
