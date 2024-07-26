#!/usr/bin/node

function fact (n) {
    if (!n) {
        return 1;
    }
    return n * fact(n - 1);
  }

  console.log(fact(process.argv[2]));
  