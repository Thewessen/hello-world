'use strict'

// A generalized version of filter
// Works on every iterable, returns an iterable

module.exports = function * (iterable, filterFunc) {
  for (const x of iterable) {
    if (filterFunc(x)) {
      yield x
    }
  }
}
