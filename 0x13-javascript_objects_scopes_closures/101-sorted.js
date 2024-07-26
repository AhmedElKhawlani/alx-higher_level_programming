#!/usr/bin/node

const data1 = require('./101-data.js').dict;
const data2 = {};

for (const key in data1) {
  if (data1[key] in data2) {
    data2[data1[key]].push(key);
  } else {
    data2[data1[key]] = [key];
  }
}
console.log(data2);
