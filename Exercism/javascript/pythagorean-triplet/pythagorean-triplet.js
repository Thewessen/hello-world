'use strict'


const genPythagorianTriples = function * () {
  const family = [[3, 4, 5]]

  // Berggren's matrices:
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

  yield family[0]

  while (true) {
    for(const matrix of [A, B, C]) {
      for (const triple of family) {
        yield triple
      }
    }
  }
  family = [A, B, C].map(
    (matrix) => family.map(
      (triple) => multiply(matrix, triple)
    )
  )
}

export class Triplet {
  constructor() {
    throw new Error("Remove this statement and implement this function");
  }

  sum() {
    throw new Error("Remove this statement and implement this function");
  }

  product() {
    throw new Error("Remove this statement and implement this function");
  }

  isPythagorean() {
    throw new Error("Remove this statement and implement this function");
  }

  static where() {
    throw new Error("Remove this statement and implement this function");
  }
}
