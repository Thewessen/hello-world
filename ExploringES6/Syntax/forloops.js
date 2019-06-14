'use strict'

const print = require('../helpers/print')

const myArr = ['Henky', 'Klaas', 'Bart', 'Wouter']

// Prior to ES5, you iterated over Arrays as follows:
print('Prior ES5 for loop:')
for (let i = 0; i < myArr.length; i += 1) {
  print(myArr[i])
}

// In ES5, you have the option of using the Array method forEach():
print()
print('ES5 forEach:')
myArr.forEach((el) => print(el))

// A for loop has the advantage that you can break from it,
// forEach() has the advantage of conciseness.
// In ES6, the for-of loop combines both advantages:
print()
print('ES6 for-of loop:')
for (const el of myArr) print(el)
