#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = process.argv[2];
  request(url, function (err, response, body) {
    if (!err) {
      console.log('code:', response.statusCode);
    }
  });
}
