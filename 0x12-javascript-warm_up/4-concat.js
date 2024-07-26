#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('undefined is undefined');
} else {
  if (args.length === 1) {
    const arg = args[0];
    const show = arg + ' is undefined';
    console.log(show);
  } else {
    const arg1 = args[0];
    const arg2 = args[1];
    const show = arg1 + ' is ' + arg2;
    console.log(show);
  }
}
