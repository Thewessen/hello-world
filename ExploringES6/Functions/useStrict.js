// Strict mode3 was introduced in ECMAScript 5 to clean up the language. It is switched on by
// putting the following line first in a file or in a function:

const print = require('../helpers/print')

const sloppyFunc = () => {
  sloppyVar = 123
}
// This creates a global var sloppyVar
sloppyFunc()
print(sloppyVar)

const strictFunc = () => {
  'use strict'
  strictVar = 123
}
// This is an error
strictFunc()
print(strictVar)
