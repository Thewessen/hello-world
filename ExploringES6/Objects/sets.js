'use strict'

const print = require('../helpers/print')

// Sets are iterables over their elements
// (which are iterated over in the same order in which they were added to the Set).
// Each element is unique:

const set = new Set().add('b').add('a').add('a')

for (let s of set) {
  print(s)
}
