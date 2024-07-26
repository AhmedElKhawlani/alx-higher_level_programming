#!/usr/bin/node

const args = process.argv.slice(2);

if (JSON.stringify(args) === '[]') {
  console.log('No argument');
} else {
  console.log(args[0]);
}
