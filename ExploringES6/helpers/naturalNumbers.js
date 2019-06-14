'use strict'

// An infinite datastream of natural numbers
module.exports = function * () {
  for (let n = 0; ; n += 1) {
    yield n
  }
}
