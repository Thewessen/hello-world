'use strict'

const print = require('../helpers/print')

// Getters and setters continue to work as they did in ECMAScript 5 (note how syntactically similar
// they are to method definitions):

const obj = {
  get first() {
    print('GET first!')
    return 'Samuel'
  },
  set last(value) {
    print('SET last!')
  }
}

obj.last = 'Thewessen'
print(obj.first)

class Person {
  constructor (first, last) {
    this._first = first
    this._last = last
  }
  set first (value) {
    print('SET firstname!')
    this._first = value
  }
  set last (value) {
    print('SET lastname!')
    this._last = value
  }
  get first () {
    print('GET firstname!')
    return this._first
  }
  get last () {
    print('GET lastname!')
    return this._last
  }
  get name () {
    return `${this.first} ${this.last}`
  }
}

const me = new Person('Sam', 'Thew')

print(me.first)
print(me.last)
print(me.name)
