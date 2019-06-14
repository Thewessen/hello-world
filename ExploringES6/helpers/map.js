'use strict'

// A generalized version of map
// Works on every iterable, returns an iterable

module.exports = function * (iterable, mapFunc) {
  for (const x of iterable) {
    yield mapFunc(x)
  }
}
