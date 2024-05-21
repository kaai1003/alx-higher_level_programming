#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  const endpoint = url + process.argv[2];
  request(endpoint, function (err, response, body) {
    if (!err) {
      body = JSON.parse(body);
      console.log(body.title);
    }
  });
}
