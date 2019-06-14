'use strict'

const print = require('../helpers/print')

// An example of an iterator iterating over the key-value-pairs of an object.

const objectEntries = (obj) => {
  let index = 0

  // In ES6, you can use strings or symbols as property keys,
  // Reflect.ownKeys() retrieves both
  const propKeys = Reflect.ownKeys(obj)

  return {
    [Symbol.iterator]() {
      return this
    },
    next () {
      if (index < propKeys.length) {
        const key = propKeys[index]
        index += 1
        return { value: [key, obj[key]] }
      } else {
        return { done: true }
      }
    }
  }
}

const first = 'Sammy'
const last = 'Thew'
const me = { first, last, [Symbol('me')]: `${first} ${last}`}

for (const kv of objectEntries(me)) {
  print(kv)
}

// or easier with a generator function

const objEnt = function * (obj) {
  for (const key of Reflect.ownKeys(obj)) {
    yield [key, obj[key]]
  }
}

for (const kv of objEnt(me)) {
  print(kv)
}
