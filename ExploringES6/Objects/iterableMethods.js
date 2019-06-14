'use strict'

const print = require('../helpers/print')

const myArr = Array.from('abcdefghi')
const mySet = new Set().add('b').add('a').add(1)
const myMap = new Map().set('a', 64).set('b', 65)

// All major ES6 data structures (Arrays, Typed Arrays, Maps, Sets) have three
// methods that return iterable objects:

//entries() returns an iterable over entries encoded as [key, value] Arrays. For Arrays, the
// values are the Array elements and the keys are their indices. For Sets, each key and value
// are the same – the Set element:
print('.entries():')
print([...myArr.entries()])
print([...mySet.entries()])
print([...myMap.entries()])

// keys() returns an iterable over the keys of the entries.
print('.keys():')
print([...myArr.keys()])
print([...mySet.keys()])
print([...myMap.keys()])

// values() returns an iterable over the values of the entries.
// Strangly enough myArr doesn't have a values method?!?
print('.values():')
print([...myArr])
print([...mySet.values()])
print([...myMap.values()])
