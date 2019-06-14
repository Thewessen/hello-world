'use strict'

const print = require('../helpers/print')

// Some new Math features in ES6:
// Math.sign() returns the sign of a number:
print(`Math.sign(3): ${Math.sign(3)}`)
print(`Math.sign(0): ${Math.sign(0)}`)
print(`Math.sign(-1): ${Math.sign(-1)}`)

// Math.trunc() removes the decimal fraction of a number:
print(`Math.trunc(1.5): ${Math.trunc(1.5)}`)
print(`Math.trunc(3.7): ${Math.trunc(3.7)}`)
print(`Math.trunc(-1.5): ${Math.trunc(-1.5)}`)
print(`Math.trunc(-3.7): ${Math.trunc(-3.7)}`)

// Math.log10() computes the logarithm to base 10:
print(`Math.log10(10): ${Math.log10(10)}`)
print(`Math.log10(10000): ${Math.log10(10000)}`)
print(`Math.log10(1337): ${Math.log10(1337)}`)

// Math.hypot() Computes the square root of the sum of the squares of its arguments
// (Pythagoras’ theorem):
print(`Math.hypot(3, 4): ${Math.hypot(3, 4)}`)
