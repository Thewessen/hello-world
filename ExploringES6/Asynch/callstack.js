'use strict'

const print = require('./helpers/print')

// When a function f calls a function g , g needs to know where to return to (inside f ) after it is
// done. This information is usually managed with a stack, the call stack. Let’s look at an example.

function h(z) {
  print(new Error().stack);
}

function g(y) {
  h(y)
}

function f(x) {
  g(x)
}

f(3)
