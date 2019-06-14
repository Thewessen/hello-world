'use strict'

const print = require('../helpers/print')
const { string: str } = require('../helpers/helpers')

// Create a new Array from an array-like object in ES6:
// This can be (Array, String, Map, Set)
const myarr = Array.from([1, 2, 3, 4])
print(str(myarr))

const myarr1 = Array.from('Hello there!')
print(str(myarr1))

const myarr2 = Array.from(new Map().set('a', 1).set('b', 2))
print(str(myarr2))

const myarr3 = Array.from(new Set().add('a').add('b'))
print(str(myarr3))

// From https://medium.com/javascript-everyday/javascript-array-from-53287c195487

// You can simply pass an object literal with a length property set to the desired
// array size, since it’s the only required property for an array-like object. If
// you only pass the first argument, the resulting array will be filled with
// undefined values. However, you can pass a project function as the second
// argument to set the desired values for array elements (e is the current
// element, whereas i is its index). It’s a far better way to accomplish the
// goal than creating an array of undefined values and calling map method, since
// it avoids creating an intermediate array.

const sizedArray = Array.from({ length: 5 }, (e, i) => i)
print(str(sizedArray))
