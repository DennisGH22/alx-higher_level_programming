#!/usr/bin/node
const dict1 = require('./101-data').dict;
const result = {};

for (const [userId, occurrences] of Object.entries(dict1)) {
  if (!Array.isArray(result[occurrences])) {
    result[occurrences] = [];
  }
  result[occurrences].push(userId);
}

console.log(result);
