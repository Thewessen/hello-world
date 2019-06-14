'use strict'

const print = require('../helpers/print')

// An iterator is a function that returns an iterable.
// Let's look at a basic example

const iterateOver = (...args) => {
  let index = 0
  const iterable = {
    [Symbol.iterator]() {
      const iterator = {
        next () {
          if (index < args.length) {
            return { value: args[index++] }
          } else {
            return { done: true }
          }
        }
      }
      return iterator
    }
  }
  return iterable
}

for (let arg of iterateOver('a', 'b', 'c')) {
  print(arg)
}

// If the iterable is the same object as the iterator,
// the syntax can be prettified:

const iterOver = (...args) => {
  let index = 0
  const iterable = {
    [Symbol.iterator]() {
      return this
    },
    next () {
      if (index < args.length) {
        return { value: args[index++] }
      } else {
        return { done: true }
      }
    }
  }
  return iterable
}

