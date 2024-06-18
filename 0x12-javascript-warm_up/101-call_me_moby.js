#!/usr/bin/node
// executes x times a function.

let i = 0;
exports.callMeMoby = function (x, theFunction) {
  for (i = 0; i < x; i++) theFunction();
};
