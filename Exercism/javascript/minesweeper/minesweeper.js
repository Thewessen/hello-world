'use strict'

const DELTAS = [
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
  [0, -1],
  [-1, -1],
  [-1, 0],
  [-1, 1]
]

export const annotate = (minefield) => minefield
  .map((row, x) => [...row].map((field, y) => {
    return field === '*'
      ? field
      : DELTAS.reduce((acc, [dx, dy]) =>
          minefield[x + dx] && minefield[x + dx][y + dy] === '*'
          ? acc + 1
          : acc, 0) || ' '
  }).join(''))
