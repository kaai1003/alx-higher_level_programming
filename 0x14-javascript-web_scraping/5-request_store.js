#!/usr/bin/node
const request = require('request');
const fs = require('fs');
if (process.argv.length === 4) {
  const url = process.argv[2];
  const filepath = process.argv[3];
  request(url, function (err, response, body) {
    if (!err) {
      fs.writeFile(filepath, body, 'utf8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}
