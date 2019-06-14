'use strict'

const print = require('../helpers/print')
const { boxFunctionOutput: str } = require('../helpers/helpers')

// ES6 classes are mostly just more convenient syntax for constructor functions.

// ES5
// =================================
function Person (name) {
  this.name = name
}
Person.prototype.describe = function () {
  return `Person called ${this.name}`
}

const sam = new Person('Samuel')
print(str('ES5', sam.describe()))

// ES6
// =================================
class Pers {
  constructor(name) {
    this.name = name
  }
  describe() {
    return `Person called ${this.name}`
  }
}

const me = new Pers('Thewessen')
print(str('ES6', me.describe()))

module.exports = {
  Person: Person,
  Pers: Pers
}
