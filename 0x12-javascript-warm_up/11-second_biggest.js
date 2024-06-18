#!/usr/bin/node
// Searches for the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
