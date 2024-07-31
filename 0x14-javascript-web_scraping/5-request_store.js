#!/usr/bin/node

const link = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request(link, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
