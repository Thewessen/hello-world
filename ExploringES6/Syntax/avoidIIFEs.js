'use strict'

const print = require('../helpers/print')
const warn = require('../helpers/warn')

// In ECMAScript 6, you can simply use a block and a let or const declaration
{
  let x = 3
}
try {
  print(x)
} catch (e) {
  warn(e)
}

// In ECMAScript 6, modules are built in, which is why the barrier to adopting them is low
// The 'local_var' from modules.js is not exposed
// NOTE: Not well support as of 06-06-2019, using require instead
const myFunc = require('../modules')
myFunc('hello')
try {
  print(localVar)
} catch (e) {
  warn(e)
}

// There is one use case where you still need an immediately-invoked function in ES6: Sometimes
// you only can produce a result via a sequence of statements, not via a single expression. If you
// want to inline those statements, you have to immediately invoke a function. In ES6, you can use
// immediately-invoked arrow functions if you want to:
const name = 'Samuel'
const reverse = (() => {
  const arr = [...name]
  arr.reverse()
  return arr.join('')
})()
print(reverse)
