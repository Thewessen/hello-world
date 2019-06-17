'use strict'

export class List {
  constructor(iterable = []) {
    if (!iterable[Symbol.iterator]) {
      throw new Error('Constructor argument is not iterable')
    }
    this.values = []
    for (const value of iterable) {
      this.append(value)
    }
    this[Symbol.iterator] = function * () {
      for (const value of this.values) {
        yield value
      }
    }
  }

  append (value) {
    // A List my not contain List-items?!?
    this.values = value instanceof List
                   ? [...this.values, ...value]
                   : [...this.values, value]
    return this
  }

  concat (iterable) {
    return new List([...this.values, ...iterable])
  }

  filter (fn, thisArg = this) {
    let newValues = new List()
    let idx = 0
    for (const value of thisArg) {
      if (fn(value, idx, thisArg)) {
        newValues.append(value)
        idx += 1
      }
    }
    return newValues
  }

  map (fn, thisArg = this) {
    let newValues = new List()
    let idx = 0
    for (const value of thisArg) {
      newValues.append(fn(value, idx, thisArg))
      idx += 1
    }
    return newValues
  }

  length () {
    let length = 0
    for (const value of this.values) {
      length += 1
    }
    return length
  }

  foldl (fn, initialValue) {
    let acc
    let idx = 0
    if (typeof initialValue !== 'undefined') {
      acc = initialValue
    } else {
      acc = this.values[idx]
      idx += 1
    }
    for (; idx < this.length(); idx += 1) {
      let curr = this.values[idx]
      acc = fn(acc, curr, idx, this)
    }
    return acc
  }

  foldr (fn, initialValue) {
    let acc
    let idx = this.length() - 1
    if (typeof initialValue !== 'undefined') {
      acc = initialValue
    } else {
      acc = this.values[idx]
      idx -= 1
    }
    for (; idx >= 0; idx -= 1) {
      let curr = this.values[idx]
      acc = fn(acc, curr, idx, this)
    }
    return acc
  }

  reverse () {
    let newValues = []
    for (let i = 0; i < this.length(); i += 1) {
      newValues = [this.values[i], ...newValues]
    }
    this.values = newValues
    return this
  }
}
