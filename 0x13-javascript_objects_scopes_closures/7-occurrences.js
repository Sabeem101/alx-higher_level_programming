#!/usr/bin/node
/*
 * Returns the number of occurences in a list.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
