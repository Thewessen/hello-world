'use strict'

const print = require('../helpers/print')

// Some generator functions need cleanup
// Like closing files that opened, etc.

// Wrong!
function * cleanUp() {
  yield 'a'
  yield 'b'
  print('Clean up!')
}
// This doesn't work if the generator is exit prematurely:
for (const clean of cleanUp()) {
  print(clean)
  break
}

// Better:
function * clean() {
  try {
    yield 'a'
    yield 'b'
  }
  finally {
    print('Clean up!')
  }
}
// This doesn't work if the generator is exit prematurely:
for (const c of clean()) {
  print(c)
  break
}
