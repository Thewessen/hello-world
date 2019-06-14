'use strict'

const print = require('../helpers/print')
const { boxFunctionOutput: str } = require('../helpers/helpers')

// A common way of naming parameters in JavaScript is via object literals (the so-called options
// object pattern). Two advantages of this approach are: Code becomes more self-descriptive
// and it is easier to omit arbitrary parameters.

// In ES5, the options param is handle like this:
const countES5 = (options) => {
  let start = options.start || 0
  let end = options.end || 10
  let step = options.step || 1
  let arr = []
  for (let i = start; i < end; i += step) {
    arr.push(i)
  }
  return arr
}
print(str('ES5', countES5({ start: 5 })))

// In ES6, you can use destructuring in parameter definitions and the code becomes simpler:
const countES6 = ({ start = 0, end = 10, step = 1 }) => {
  let arr = []
  for (let i = start; i < end; i += step) {
    arr.push(i)
  }
  return arr
}
print(str('ES6', countES6({ start: 3, end: 7 })))
