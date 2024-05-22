#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = process.argv[2];
  request(url, function (err, response, body) {
    if (!err) {
      const userTasks = {};
      body = JSON.parse(body);
      for (const task of body) {
        if (task.completed) {
          if (task.userId in userTasks) {
            userTasks[task.userId] = userTasks[task.userId] + 1;
          } else {
            userTasks[task.userId] = 1;
          }
        }
      }
      console.log(userTasks);
    }
  });
}
