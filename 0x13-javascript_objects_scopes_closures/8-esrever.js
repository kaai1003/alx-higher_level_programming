#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  let j = 0;
  const reversedList = [];
  while (i >= 0) {
    reversedList[j] = list[i];
    i--;
    j++;
  }
  return reversedList;
};
