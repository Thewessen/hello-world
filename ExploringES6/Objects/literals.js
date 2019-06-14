'use strict'

const print = require('../helpers/print')
const printObj = require('../helpers/objectEntries')

// Besides classes, which are the major OOP feature, ES6 has some new syntax
// and shorthands for objects:
// - method definition
// - shorthands
// - compute property keys

const propkey = 'name'
const first = 'Samuel'
const last = 'Thewessen'

const obj = {
  callme () {
    return `${first} ${last}`
  },
  ['ab' + 'cd']: 'something',
  [propkey]: `${this.first} ${this.last}`,
  first,
  last,
  ['a' + 'ge']() {
    return 22
  }
}
const place = 'Amsterdam'
Object.assign(obj, { place })

printObj(obj)
print(obj.callme())
print(obj.age())

print(JSON.stringify(obj))
