#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = process.argv[2];
  const id = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;
  request(url, function (err, response, body) {
    if (!err) {
      body = JSON.parse(body);
      const details = body.results;
      for (const episode of details) {
        const arr = episode.characters;
        for (const char of arr) {
          if (char === id) {
            count += 1;
          }
        }
      }
      console.log(count);
    }
  });
}
