#!/usr/bin/node

const array = require('./100-data.js').list;
const newList = array.map(function (x, index) {
  return (x * index);
});
console.log(array);
console.log(newList);
