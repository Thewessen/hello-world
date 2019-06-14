'use strict'

const print = require('../helpers/print')
const { boxFunctionOutput: str } = require('../helpers/helpers')

// In ES5, if you want a function (or method) to accept an arbitrary number of arguments, you must
// use the special variable arguments:
const giveArgumentsES5 = () => {
  let args = [].slice.call(arguments, 1)
  return args
}
print(str('ES5', giveArgumentsES5(1, 2, 3, 4, 5)))

// In ES6, you can declare a rest parameter ( args in the example below) via the ... operator:
const giveArgumentsES6 = (...args) => args
const printGiveArgumentsES6 = nicePrint('Rest arguments ES6:', giveArgumentsES6)
print(str('ES6', giveArgumentsES6(1, 2, 3, 4, 5)))
