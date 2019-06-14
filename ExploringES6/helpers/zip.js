'use strict'

const isFunction = require('./isFunction')

// Pythons zip function in Javascript
module.exports = function * (...iterables) {
  const iters = iterables.map((i) => i[Symbol.iterator]())
  let done = false
  while (!done) {
      const items = iters.map((i) => i.next())
      done = items.some((item) => item.done)
      if (!done) {
        yield items.map((i) => i.value)
      }
  }
  for (const iter of iters) {
    isFunction(iter.return) && iter.return()
  }
}
