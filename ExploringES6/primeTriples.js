'use strict'

const sum = (a, b) => a + b
const product = (a, b) => a * b

const multiplyMatrix = (matrix, vector) =>
  matrix.map(
    (row) => row.map((n, idx) => n * vector[idx])
  ).map((row) => row.reduce(sum))

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
  while (true) {
    for (const triplet of family) {
      for (const matrix of [A, B, C]) {
        yield new Triplet(...multiplyMatrix(matrix, triplet.triple))
      }
    }
    yield * family
    family = multiplyMatricesTriplets([A, B, C], family)
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

const takeWhile = function * (iterable, ...fns) {
  for (const value of iterable) {
    if (fns.some((fn) => !fn(value))) {
      break
    }
    yield value
  }
}

module.exports = filter(
  takeWhile(
    EUCLIDTRIPLES(),
    (triplet) => triplet.triple.every((v) => v <= 100),
  ),
  (triplet) => triplet.triple.every((v) => v > 10),
)
