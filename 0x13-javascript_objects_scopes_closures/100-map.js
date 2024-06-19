#!/usr/bin/node
/*
 * Imports an array and computes a new array.
 */
const nlist = require('./100-data.js').list;
console.log(nlist);
console.log(nlist.map((item, index) => item * index));
