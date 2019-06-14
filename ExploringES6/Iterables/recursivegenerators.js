'use strict'

const print = require('../helpers/print')

// Yield* makes recursive generator calls possible:
function * gen1 () {
  yield 'a'
  yield 'b'
}

function * gen2 () {
  yield 'c'
  yield 'd'
}

function * genTwo () {
  yield * gen1()
  yield * gen2()
}

for (const x of genTwo()) {
  print(x)
}
