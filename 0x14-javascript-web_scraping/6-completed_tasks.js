#!/usr/bin/node

const request = require('request');
const API = process.argv[2];

request(API, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (let i = 0; i < tasks.length; i++) {
      const task = tasks[i];
      if (task.completed) {
        const Id = task.userId;
        if (Id in completed) {
          completed[Id] = completed[Id] + 1;
        } else {
          completed[Id] = 1;
        }
      }
    }
    console.log(completed);
  }
});
