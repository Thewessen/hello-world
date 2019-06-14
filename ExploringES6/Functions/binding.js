'use strict'

const print = require('../helpers/print')

// Arrowfunction in ES6 bind very loosly
const f = (x) => (x % 2) === 0 ? x : 0
print(f(5))

// wrong
// print(typeof () => {})

// correct
print(typeof (() => {}))

const g = (x) => typeof x
print(g(function() {}))
print(g(() => {}))
