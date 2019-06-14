'use strict'

const print = require('../helpers/print')

// In ES6, the new Number.isNaN() provides a safe way to detect NaN specific.
// (because it doesn’t coerce non-numbers to numbers):

print(`isNaN('abc'): ${isNaN('abc')}`)
print(`Number.isNaN('abc'): ${Number.isNaN('abc')}`)
print(`Number.isNaN(NaN): ${Number.isNaN(NaN)}`)

// This is helpfull for searching NaN specifically
const myarr = [1, 'ab', NaN]
print(`[${myarr}].indexOf(NaN): ${myarr.indexOf(NaN)}`)
print(`[${myarr}].findIndex((x) => Number.isNaN(x)): `
      + `${myarr.findIndex((x) => Number.isNaN(x))}`)
