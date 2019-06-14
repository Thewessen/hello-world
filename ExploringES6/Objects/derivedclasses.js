'use strict'

const print = require('../helpers/print')
const { boxFunctionOutput: str } = require('../helpers/helpers')
const { Person, Pers } = require('./classes')

// ES6 classes are mostly just more convenient syntax for constructor functions.

// ES5
// =================================
function Employee (name, title) {
  Person.call(this, name)
  this.title = title
}
Employee.prototype = Object.create(Person.prototype)
Employee.prototype.constructor = Employee
Employee.prototype.describe = function () {
  // calling the super discribe first
  return `${Person.prototype.describe.call(this)} (${this.title})`
}

const worker = new Employee('Samuel', 'junior')
print(str('ES5', worker.describe()))

// ES6
// =================================
class Emp extends Pers {
  constructor(name, title) {
    super(name)
    this.title = title
  }
  describe() {
    return `${super.describe()} (${this.title})`
  }
}

const meWorker = new Emp('Thewessen', 'Senior')
print(str('ES6', meWorker.describe()))
