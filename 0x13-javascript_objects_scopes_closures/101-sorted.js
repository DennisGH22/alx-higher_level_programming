#!/usr/bin/node
const originalDict = require('./101-data').dict;
const result = {};

for (const userId in originalDict) {
  const occurrences = originalDict[userId];

  if (!result[occurrences]) {
    result[occurrences] = [];
  }

  result[occurrences].push(userId);
}

console.log(result);
