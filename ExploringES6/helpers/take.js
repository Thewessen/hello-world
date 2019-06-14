'use strict'

// Taking from an iterable
module.exports = function * (n, iterable) {
  for (const x of iterable) {
    if (n <= 0) return
    n -= 1
    yield x
  }
}
