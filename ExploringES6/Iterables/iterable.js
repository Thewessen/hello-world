'use strict'

const print = require('../helpers/print')

// In ES6, if an object contains the special Symbol.iterator property key,
// the object is suposed to be iterable.
// Let’s first implement a dummy iterable to get a feeling for how iteration works.

const iterable = {
  [Symbol.iterator]() {
    let step = 0
    const iterator = {
      next () {
        if (step <= 2) {
          step += 1
        }
        switch (step) {
          case 1:
            return { value: 'hello', done: false }
          case 2:
            return { value: 'world', done: false }
          case 3:
            return { value: undefined, done: true }
        }
      }
    }
    return iterator
  }
}

for (const t of iterable) {
  print(t)
}

// Some improvements:
// - if value is undefined, it can be ommited
