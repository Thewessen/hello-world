'use strict'

const print = require('../helpers/print')
const { boxFunctionOutput: str } = require('../helpers/helpers')

// In ES5, you specify default values for parameters like this:
const coords = (x, y) => {
  x = x || 0
  y = y || 0
  return `(${x}, ${y})`
}
print(str('Default params in ES5:', coords(3, false)))
// Note that the default value is triggered by any falsy value!

// An added benefit is that in ES6, a parameter default value
// is only triggered by undefined!
// The syntax is nicer:
const coordsDefault = (x = 0, y = 0) => `(${x}, ${y})`
print(str('Default params in ES6:', coordsDefault(3, false)))
print(str('Default params in ES6', coordsDefault(3)))
