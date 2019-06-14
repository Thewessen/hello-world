'use strict'

const print = require('./helpers/print')
const { string: str } = require('./helpers/helpers')

// Every time you call the factory function, a new and unique symbol is created. The optional
// parameter is a descriptive string that is shown when printing the symbol (it has no other purpose):

const mySymbol = Symbol('keyOfObject')
print(mySymbol)

// Use case 1: unique property keys
// Create an iterable object using the Symbol.iterator.
const myarr = [0, 1, 2, 3, 4, 5, 6]

const reverse = (arr) => ({
  [Symbol.iterator]() {
    let i = arr.length
    return {
      next: () => {
        i -= 1
        return {
          value: arr[i],
          done: i < 0
        }
      }
    }
  }
})
      
print(str([...reverse(myarr)]))

// print(str(iterableObject))
// for (const key of iterableObject) {
//   print(key)
// }
