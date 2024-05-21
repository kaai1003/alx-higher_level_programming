#!/usr/bin/node
const fs = require('fs');
if (process.argv.length === 3) {
  const filename = process.argv[2];
  fs.readFile(filename, 'utf8', (err, content) => {
    if (err) {
      console.error(err);
    } else {
      console.log(content);
    }
  });
}
