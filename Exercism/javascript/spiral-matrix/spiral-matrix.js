'use strict'

const range = function * (from, to) {
  if (from <= to) {
    yield from
    yield* range(from + 1, to)
  }
}

const turn = ([dx, dy]) => {
  if (dx !== 0) {
    return [0, dx]
  }
  return [0 - dy, 0]
}

const move = ([x, y], ...moves) => {
  for (const [dx, dy] of moves) {
    [x, y] = [x + dx, y + dy]
  }
  return [x, y]
}

const value = ([x, y], matrix) =>
  matrix[y] ? matrix[y][x] : undefined

const newMatrix = (size) =>
  Array.from({ length: size }, () => Array(size).fill(null))

const spiral = (start, [dx, dy], numbers, matrix) => {
  let next = start
  while (value(next, matrix) === null) {
    const [a, b] = next
    matrix[b][a] = numbers.next().value
    next = move(next, [dx, dy])
  }
  next = move(next, [0 - dx, 0 - dy], turn([dx, dy]))
  if (value(next, matrix) === null) {
    return spiral(next, turn([dx, dy]), numbers, matrix)
  }
  return matrix
}

export const SpiralMatrix = {
  ofSize (n) {
    return spiral([0, 0], [1, 0], range(1, n ** 2), newMatrix(n))
  }
}
