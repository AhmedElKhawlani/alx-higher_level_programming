#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  let max1 = parseInt(args[0], 10);
  let max2 = parseInt(args[1], 10);
  if (max2 > max1) {
    const alt = max1;
    max1 = max2;
    max2 = alt;
  }
  for (let i = 2; i < args.length; i++) {
    const n = parseInt(args[i], 10);
    if (n > max1) {
      max2 = max1;
      max1 = n;
    } else if (n > max2) {
      max2 = n;
    }
  }
  console.log(max2);
}
