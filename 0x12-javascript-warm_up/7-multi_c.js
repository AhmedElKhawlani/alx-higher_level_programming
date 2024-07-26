#!/usr/bin/node

let test = 1;
const args = process.argv.slice(2);

if (args.length === 0) {
  test = 0;
} else if (isNaN(parseInt(args[0], 10))) {
  test = 0;
}
if (test === 0) {
  console.log('Missing number of occurrences');
} else {
  const n = parseInt(args[0], 10);
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
