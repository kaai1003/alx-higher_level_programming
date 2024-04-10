#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let sb = process.argv[2];
  let big = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (i === 3) {
      if (parseInt(process.argv[i]) > big) {
        big = process.argv[i];
      } else {
        sb = process.argv[i];
      }
    } else {
      if (parseInt(process.argv[i]) > big) {
        sb = big;
        big = process.argv[i];
      } else if (parseInt(process.argv[i]) > sb) {
        sb = process.argv[i];
      }
    }
  }
  console.log(sb);
}
