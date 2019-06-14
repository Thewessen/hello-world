'use strict'
// In ES6, you can additionally declare variables via let and const . Such variables are block-scoped,
// their scopes are the innermost enclosing blocks. let is roughly a block-scoped version of var .
// const works like let , but creates variables whose values can’t be changed.

const print = require('../helpers/print')
const warn = require('../helpers/warn')

// Example with var
var x = 3
function varfunc (randomize) {
  if (randomize) {
    var x = Math.random()
    return x
  }
  return x
}
print('Example with var')
print(varfunc(false))  // undefined

// Example with var
let y = 3
function letfunc (randomize) {
  if (randomize) {
    let y = Math.random()
    return y
  }
  return y
}
print('Example with let')
print(letfunc(false)) // 3


const z = 3
try {
  z = 5
} catch (error) {
  warn(error)
}
