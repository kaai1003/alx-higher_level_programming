#!/usr/bin/node
const fs = require('fs');
if (process.argv.length === 4) {
  const filename = process.argv[2];
  const content = process.argv[3];
  fs.writeFile(filename, content, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}
