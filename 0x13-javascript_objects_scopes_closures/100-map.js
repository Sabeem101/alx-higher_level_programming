#!/usr/bin/node
/*
 * Imports an array and computes a new array.
 */
const new_list = require('./100-data.js').list;
console.log(new_list);
console.log(new_list.map((item, index) => item * index));
