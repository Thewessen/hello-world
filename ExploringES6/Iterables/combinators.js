'use strict'

const print = require('../helpers/print')
const isFunction = require('./isFunction')

// Combinators are functions that combine existing iterables to create new ones.

const takeIterator = (n, iterable) => {
  const iter = iterable[Symbol.iterator]()
  return {
    [Symbol.iterator] () {
      return this
    },
    next () {
      if (n > 0) {
        n -= 1
        return iter.next()
      } else {
        return { done: true }
      }
    }
  }
}

const myArr = Array.from('abcdefg')
const iter = takeIterator(4, myArr)
for (const x of iter) {
  print(x)
  break
}

// Because the iterator doesn't contain a return() method,
// The iterator is not closed
print('second for-of-loop')
for (const x of iter) {
  print(x)
}

// Much nicer in a generator function
const take = function * (n, iterable) {
  const iter = iterable[Symbol.iterator]()
  while (n > 0) {
    n -= 1
    yield iter.next().value
  }
}
    
for (const x of take(3, myArr)) {
  print(x)
}

// Another example of a combinator
// Pythons zip function in Javascript
const zip = (...iterables) => {
  const iters = iterables.map((i) => i[Symbol.iterator]())
  let done = false
  return {
    [Symbol.iterator]() {
      return this
    },
    next() {
      if (!done) {
        const items = iters.map((i) => i.next())
        done = items.some((item) => item.done)
        if (!done) {
          return { value: items.map((i) => i.value) }
        }
        // If done, do cleanup
        for (const iter of iters) {
          isFunction(iter.return) && iter.return()
        }
      }
      return { done: true }
    }
  }
}

const alpha = Array.from('abcdef')
const beta = Array.from('123456')

for (let t of zip(alpha, beta)) {
  console.log(t)
}

// For a generator example take a look at ../helpers/zip.js
