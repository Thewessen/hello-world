'use strict'

const sum = (a, b) => a + b
const product = (a, b) => a * b

const numbers = function * (from, too = Number.POSITIVE_INFINITY, step = 1) {
  for (let i = from; i < too; i += step) {
    yield i
  }
}

const GENTRIPLES = function * (max) {
  for (const a of numbers(1, max)) {
    for (const b of numbers(a, max)) {
      const t = new Triplet(a, b, Math.hypot(a, b))
      if (t.isPythagorean()) {
        yield t
      }
    }
  }
}

const filter = function * (iterable, ...fns) {
  for (const value of iterable) {
    if (fns.every((fn) => fn(value))) {
      yield value
    }
  }
}

export class Triplet {
  constructor (...triple) {
    this.triple = triple.sort((a, b) => a - b)
  }

  sum () {
    return this.triple.reduce(sum)
  }

  product () {
    return this.triple.reduce(product)
  }

  isPythagorean () {
    const t = this.triple
    const [a, b, c] = t
    return t.length === 3 &&
      t.every(Number.isInteger) &&
      a ** 2 + b ** 2 === c ** 2
  }

  static where ({ sum, minFactor = 0, maxFactor }) {
    if (!maxFactor) {
      throw new Error('maxFactor not set')
    }
    const triplets = filter(
      GENTRIPLES(maxFactor),
      (t) => t.triple.every((v) => v > minFactor)
    )
    return sum && sum > 0
      ? [...filter(triplets, (t) => t.sum() === sum)]
      : [...triplets]
  }
}
