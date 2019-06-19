'use strict'

const isEven = (int) => !!(int % 2)

const collatzConjecture = function * (n) {
  if (!Number.isInteger(n) || n <= 0) {
    throw new Error('Collatz Conjecture works on positive integers n')
  }
  if (n === 1) return n
  do {
    n = isEven(n)
      ? n / 2
      : 3 * n + 1
    yield n
  } while (n !== 1)
}

const size = (iterable) => [...iterable].length

export const steps = (n) => {
  if (!Number.isInteger(n) || n <= 0) {
    throw new Error('Only positive numbers are allowed')
  }
  return size(collatzConjecture(n))
}
