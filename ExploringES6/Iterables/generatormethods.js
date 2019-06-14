'use strict'

const print = require('../helpers/print')

// Generator methods in ES6
const obj = {
  * count(till) {
      for (let i = 0; i < till; i += 1) {
        yield i
      }
  }
}

print([...obj.count(10)])
