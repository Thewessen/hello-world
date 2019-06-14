'use strict'

const print = require('../helpers/print')
const { string: str } = require('../helpers/helpers')

// In ES6, you can use the fill method of an Array to all empty spots of an
// Array:
const myarr = Array(3).fill('x')
print(str(myarr))
