#!/usr/bin/node
const fs = require('fs');

function concatFiles (file1, file12, destination) {
  const file1Content = fs.readFileSync(file1, 'utf-8');

  const file2Content = fs.readFileSync(file12, 'utf-8');

  const concatenatedContent = `${file1Content}\n${file2Content}`;

  fs.writeFileSync(destination, concatenatedContent);
}

const file1 = process.argv[2];
const file12 = process.argv[3];
const destination = process.argv[4];

concatFiles(file1, file12, destination);
