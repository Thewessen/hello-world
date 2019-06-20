'use strict'

const numbers = function * (till) {
  for (let i = 1; i < till + 1; i += 1) {
    yield i
  }
}

const sum = (a, b) => a + b

export class Squares {
  constructor (nr) {
    this._sumOfSquares = Array
      .from(numbers(nr))
      .map((nr) => nr ** 2)
      .reduce(sum)
    this._squareOfSum = Array
      .from(numbers(nr))
      .reduce(sum) ** 2
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
}
