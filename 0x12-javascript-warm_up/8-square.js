#!/usr/bin/node
const sq = 'X';
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < size) {
    console.log(sq.repeat(size));
    i++;
  }
}
