'use strict'

export class Squares {
  constructor (to) {
    const { numbers, squared, sum, value, compose } = this
    this._sumOfSquares = compose(
      numbers,
      squared,
      sum,
      value
    )(to)
    this._squareOfSum = compose(
      numbers,
      sum,
      squared,
      value
    )(to)
  }

  get sumOfSquares () {
    return this._sumOfSquares
  }

  get squareOfSum () {
    return this._squareOfSum
  }

  get difference () {
    return this._squareOfSum - this._sumOfSquares
  }

  * numbers (till) {
    for (let i = 1; i < till + 1; i += 1) {
      yield i
    }
  }

  * squared (iterable) {
    for (const n of iterable) {
      yield n ** 2
    }
  }

  * sum (iterable) {
    let sum = 0
    for (const n of iterable) {
      sum += n
    }
    yield sum
  }

  value (iterable) {
    const { value } = iterable.next()
    return value
  }

  compose (...fns) { 
    return (value) => {
      for (const fn of fns) {
        value = fn(value)
      }
      return value
    }
  }
}
