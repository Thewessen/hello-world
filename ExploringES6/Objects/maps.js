'use strict'

const print = require('../helpers/print')

// New iterable objects called Maps.
// Maps are iterables over their entries.
// Each entry is encoded as a [key, value] pair, an Array with two elements.
// The entries are always iterated over deterministically, in the same order in which
// they were added to the map.

const map = new Map().set('a', 64).set('b', 65)

for (let [key, value] of map) {
  print(`[${key}, ${value}]`)
}
