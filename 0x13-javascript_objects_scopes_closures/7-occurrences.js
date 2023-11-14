#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
