'use strict'

const print = require('../helpers/print')

// Checks if a number is an integer
print(`4: ${Number.isInteger(4)}`)
print(`-4: ${Number.isInteger(-4)}`)
print(`1.2: ${Number.isInteger(1.2)}`)
print(`NaN: ${Number.isInteger(NaN)}`)
