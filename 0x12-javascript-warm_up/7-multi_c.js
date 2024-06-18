#!/usr/bin/node
// Prints x times 'C is fun'.

let a = 0;
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (a = 0; a < x; a++) {
    console.log('C is fun');
  }
}
