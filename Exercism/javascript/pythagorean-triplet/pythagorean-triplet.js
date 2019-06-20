'use strict'

const sum = (a, b) => a + b
const product = (a, b) => a * b

const multiplyMatrix = (matrix, vector) =>
  matrix.map(
    (row) => row.map(
      (n, idx) => n * vector[idx]
    )
  )
  .map((row) => row.reduce(sum))

const newBerggrenTriplesGen = function * (vectors) {
  // Berggren's matrices
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

const newEuclidTripleGen = function * (triple) {

}

const genPythagorianTriples = function * () {
  let family = [[3, 4, 5]]
  yield family[0]
  while (true) {
    family = [...newBerggrenTriplesGen(family)]
    yield * family
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
  let count = 0
  let triple
  for (triple of genPythagorianTriples()) {
    if (triple.reduce(sum) === 180) {
      break
    }
    count += 1
  }
  return [count, triple]
}

module.exports = checkPyth

