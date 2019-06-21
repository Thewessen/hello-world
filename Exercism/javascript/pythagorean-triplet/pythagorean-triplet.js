'use strict'

const sum = (a, b) => a + b
const product = (a, b) => a * b

const multiplyMatrix = (matrix, vector) =>
  matrix.map(
    (row) => row.map((n, idx) => n * vector[idx])
  ).map((row) => row.reduce(sum))

const BERGRENTRIPLES = function * (vectors) {
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

  for (const vector of vectors) {
    for (const matrix of [A, B, C]) {
      yield multiplyMatrix(matrix, vector)
    }
  }
}

const numbers = function * (from, too, step) {
  for (let i = from; i < too; i += step) {
    yield i
  }
}

const GCD = (a, b) => {
  [a, b] = [a, b].sort((a, b) => a < b)
  const rest = a % b
  return rest === 0
    ? b
    : GCD(b, rest)
}

const isEven = (a) => a % 2 === 0
const notBothOdd = (a) => (b) => isEven(a) || isEven(b)
const coPrime = (a) => (b) => GCD(a, b) === 1

const filter = function * (iterable, ...fns) {
  for (const value of iterable) {
    if (fns.every((fn) => fn(value))) {
      yield value
    }
  }
}
const newEuclidTripleGen = function * (triple) {
  const a = (m, n) => 2 * m * n
  const b = (m, n) => m ** 2 - n ** 2
  const c = (m, n) => m ** 2 + n ** 2
  for (const m of numbers(2, Number.POSITIVE_INFINITY, 1)) {
    for (const n of filter(numbers(1, m, 1), coPrime(m), notBothOdd(m))) {
      yield [a, b, c].map(f => f(m, n))
    }
  }
}

const genPythagorianTriples = function * () {
  let family = [[3, 4, 5]]
  const gen = BERGRENTRIPLES
  while (true) {
    yield * gen(family)
    family = gen(family)
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
    throw new Error("Remove this statement and implement this function");
  }
}
const take = function * (count, iterable) {
  const gen = iterable[Symbol.iterator]()
  for (let i = 0; i < count; i++) {
    const { value, done } = gen.next()
    if (done) {
      break
    }
    yield value
  }
}

const checkPyth = () => {
  // let count = 0
  // let triple
  for (const triple of take(10, genPythagorianTriples())) {
    console.log(triple)
    // if (triple.reduce(sum) === 180) {
    //   break
    // }
    // count += 1
  }
  // return [count, triple]
}

module.exports = GCD

