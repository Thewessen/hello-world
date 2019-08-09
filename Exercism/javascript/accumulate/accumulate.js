'use strict'

class Collection {
  constructor (iterable) {
    this.collection = [...iterable]
  }

  map (fn) {
    const result = []
    for (const el of this.collection) {
      result.push(fn(el))
    }
    return result
  }
}

export const accumulate = (arr, fn) => Collection(arr).map(fn)
