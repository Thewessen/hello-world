'use strict'

const range = function * (to) {
  for (let i = 1; i < to; i += 1) {
    yield i
  }
}

const turn = ([dx, dy]) => {
  if (dx === 1 && dy === 0) {
    return [0, -1]
  }
  if (dx === 0 && dy === -1) {
    return [-1, 0]
  }
  if (dx === -1 && dy === 0) {
    return [0, 1]
  }
  return [1, 0]
}

const move = ([x, y], ...moves) => {
  for (const [dx, dy] of moves) {
    [x, y] = [x + dx, y + dy]
  }
  return [x, y]
}

const newMatrix = (size) => Array(size).fill(Array(size).fill(null))

const spiral = ([x, y], [dx, dy], numbers, matrix) => {
  let [a, b] = [x, y]
  while (matrix[b] && matrix[b][a] === null) {
    matrix[b][a] = numbers.next().value
    [a, b] = move([a, b], [dx, dy])
  }
  // console.log([a, b], [0 - dx, 0 - dy], turn([dx, dy]))
  [a, b] = move([a, b], [0 - dx, 0 - dy], turn([dx, dy]))
  if (matrix[b][a] === null) {
    return spiral([a, b], turn([dx, dy]), numbers, matrix)
  }
  return matrix
}

module.exports = spiral([0, 0], [1, 0], range(4 * 4), newMatrix(4))
// module.exports = move([0, 0], [3, 0])

const SpiralMatrix = {
  ofSize (n) {
    this.size = n
  }
}
