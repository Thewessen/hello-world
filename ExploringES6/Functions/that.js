'use strict'

const print = require('../helpers/print')

// Test for this value

print('inside function()')
function f () {
  print(this)
}
f()

print('inside () => {}')
const g = () => print(this)
g()

print('inside function return function()')
function h () {
  return function () {
    print(this)
  }
}
(h())()

print('inside function return () => {}')
function k () {
  return () => print(this)
}
(k())()

print('inside () => {} return () => {}')
const m = () => (() => print(this))
const n = m()
n()
