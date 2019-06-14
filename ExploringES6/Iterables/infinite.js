'use strict'

const print = require('../helpers/print')
const take = require('../helpers/take')

// Let's look at a iterator that never stops
function naturalNumbers () {
  let n = 0
  return {
    [Symbol.iterator] () {
      return this
    },
    next () {
      return { value: n += 1 }
    }
  }
}

for (const n of take(4, naturalNumbers())) {
  print(n)
}

// In a generator
function * natural () {
  for (let n = 0; ; n += 1) {
    yield n
  }
}

for (const n of take(6, natural())) {
  print(n)
}

