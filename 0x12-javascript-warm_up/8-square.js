#!/usr/bin/node
// Prints a square.

let a = 0;
let b = 0;
let row = '';
const p = parseInt(process.argv[2]);
if (isNaN(p)) {
  console.log('Missing size');
} else {
  while (a < p) {
    row += 'X';
    a++;
  }
  while (b < p) {
    console.log(row);
    b++;
  }
}
