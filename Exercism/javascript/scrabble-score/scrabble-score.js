'use strict'

const inverseKeyValues = (acc, curr) =>
  [...acc, ...curr[1].map(
    (char) => [char, curr[0]]
  )]

const SCORES = new Map([
  [1, ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']],
  [2, ['D', 'G']],
  [3, ['B', 'C', 'M', 'P']],
  [4, ['F', 'H', 'V', 'W', 'Y']],
  [5, ['K']],
  [8, ['J', 'X']],
  [10, ['Q', 'Z']]
].reduce(inverseKeyValues, []))

const sum = (acc, curr) => acc + curr

export const score = (word) =>
  word === ''
    ? 0
    : word
      .toUpperCase()
      .split('')
      .map(char => SCORES.get(char))
      .reduce(sum)
