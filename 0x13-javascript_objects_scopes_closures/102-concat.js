#!/usr/bin/node
const fs = require('fs');

function concatFiles (file1, file2, destination) {
  const file1Content = fs.readFileSync(file1, 'utf-8');

  const file2Content = fs.readFileSync(file2, 'utf-8');

  const concatenatedContent = file1Content + file2Content;

  fs.writeFileSync(destination, concatenatedContent);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

concatFiles(file1, file2, destination);
