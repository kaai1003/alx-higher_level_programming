#!/usr/bin/node
if (process.argv.length < 4) {
    console.log(0);
  } else {
    let b = process.argv[2];
    let sb = -Infinity;
    for (let i = 3; i < process.argv.length; i++) {
      if (process.argv[i] > b) {
        sb = b;
        b = process.argv[i];
      } else if (process.argv[i] < b && process.argv[i] > sb) {
        sb = process.argv[i];
      }
    }
    console.log(sb);
  }
  