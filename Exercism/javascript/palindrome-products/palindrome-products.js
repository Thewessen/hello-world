'use strict'

const product = (a, b) => a * b

const isPalindromeFactor = (pair) => pair
  .reduce(product)
  .toString()
  .split('')
  .reverse()
  .join('') === pair.reduce(product).toString()

const range = function * (from, to, step) {
  for (let i = from; i <= to; i += step) {
    yield i
  }
}
const genFactors = function * (from, to, step) {
  for (const a of range(from, to - 1, step)) {
    for (const b of range(a, to, step)) {
      yield [a, b]
    }
  }
}

const filterGen = function * (iterable, fn) {
  for (const value of iterable) {
    if (fn(value)) {
      yield value
    }
  }
}

const groupFactors = (factors) => factors
  .reduce((prod, pair, __, arr) => {
    const p = pair.reduce(product)
    if (prod.includes(p)) {
      return prod
    }
    return [...prod, [p, arr.filter((sec) => sec.reduce(product) === p)]]
  }, []).sort((a, b) => a[0] - b[0])

export class Palindromes {
  static generate ({ maxFactor, minFactor = 1 }) {
    if (minFactor > maxFactor) {
      throw new Error('min must be <= max')
    }
    const factors = groupFactors([...filterGen(genFactors(minFactor, maxFactor, 1), isPalindromeFactor)])
    const resultLength = factors.length
    const def = { value: null, factors: [] }
    return resultLength > 0
      ? { 
          smallest: {
            value: factors[0][0],
            factors: factors[0][1]
          },
          largest: {
            value: factors[resultLength-1][0],
            factors: factors[resultLength-1][1]
          }
        }
      : {
          smallest: def,
          largest: def
        }
  }
}
