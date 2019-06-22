'use strict'

const sum = (a, b) => a + b
const product = (a, b) => a * b

const multiplyMatrix = (matrix, triplet) =>
  matrix.map(
    (row) => row.map((n, idx) => n * triplet.triple[idx])
  ).map((row) => row.reduce(sum))

const multiplyMatrices = function * (matrices, triplets) {
  for (const triplet of triplets) {
    for (const matrix of matrices) {
      yield multiplyMatrix(matrix, triplet)
    }
  }
}

const BERGRENTRIPLES = function * (triplet) {
  const A = [
    [-1, 2, 2],
    [-2, 1, 2],
    [-2, 2, 3]]
  const B = [
    [1, 2, 2],
    [2, 1, 2],
    [2, 2, 3]]
  const C = [
    [1, -2, 2],
    [2, -1, 2],
    [2, -2, 3]]

  let family = [triplet]
  do {
    yield * family
    family = multiplyMatrices([A, B, C], family)
  } while (true)
}

const numbers = function * (from, too = Number.POSITIVE_INFINITY, step = 1) {
  for (let i = from; i < too; i += step) {
    yield i
  }
}

const GCD = (a, b) => {
  if (a < b) {
    [a, b] = [b, a]
  }
  const rest = a % b
  return rest === 0
    ? b
    : GCD(b, rest)
}

const isEven = (a) => a % 2 === 0
const notBothOdd = (a) => (b) => isEven(a) || isEven(b)
const coPrimeWith = (a) => (b) => GCD(a, b) === 1

const filter = function * (iterable, ...fns) {
  for (const value of iterable) {
    if (fns.every((fn) => fn(value))) {
      yield value
    }
  }
}

const EUCLIDTRIPLES = function * () {
  const a = (m, n) => 2 * m * n
  const b = (m, n) => m ** 2 - n ** 2
  const c = (m, n) => m ** 2 + n ** 2
  for (const m of numbers(2)) {
    for (const n of filter(numbers(1, m), coPrimeWith(m), notBothOdd(m))) {
      yield new Triplet(...[a, b, c].map(f => f(m, n)))
    }
  }
}

class Triplet {
  constructor(...triple) {
    this.triple = triple
  }

  sum() {
    return this.triple.reduce(sum)
  }

  product() {
    return this.triple.reduce(product)
  }

  isPythagorean() {
    const [a, b, c] = this.triple.sort((a, b) => a > b)
    return this.triple.length === 3 &&
      Math.round(Math.hypot(a, b)) === c
  }

  static where ({ sum, minFactor, maxFactor}) {
  }
}

const take = function * (count, iterable) {
  const gen = iterable[Symbol.iterator]()
  for (let i = 0; i < count; i += 1) {
    const { value, done } = gen.next()
    if (done) {
      break
    }
    yield value
  }
}

module.exports = take(100, EUCLIDTRIPLES())
// module.exports = take(100, BERGRENTRIPLES(new Triplet(3, 4, 5)))
