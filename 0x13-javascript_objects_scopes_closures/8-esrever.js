#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const array = [];
  for (let i = len - 1; i >= 0; i--) {
    array.push(list[i]);
  }
  return array;
};
