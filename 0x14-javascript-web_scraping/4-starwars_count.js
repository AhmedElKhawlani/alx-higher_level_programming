#!/usr/bin/node

const request = require('request');
const API = process.argv[2];
const people = 'https://swapi-api.alx-tools.com/api/people/18/';

request(API, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < movies.length; i++) {
      const movie = movies[i];
      const actors = movie.characters;
      if (actors.include(people)) {
        count = count + 1;
      }
    }
  }
});
