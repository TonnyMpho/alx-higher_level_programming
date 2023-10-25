#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);

    const taskCompleted = {};

    tasks.forEach(task => {
      if (task.completed === true) {
        const userId = task.userId;

        if (taskCompleted[userId]) {
          taskCompleted[userId] += 1;
        } else {
          taskCompleted[userId] = 1;
        }
      }
    });
    console.log(taskCompleted);
  }
});
