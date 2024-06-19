#!/usr/bin/node
/*
 * Imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence.
 */
const dicts = require('./101-data.js').dict;
const ndict = {};
for (const key in dicts) {
  if (ndict[dicts[key]] === undefined) {
    ndict[dicts[key]] = [];
  }
  ndict[dicts[key]].push(key);
}
console.log(ndict);
