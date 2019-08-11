'use strict'

export const validate = (number) => number
  .toString()
  .split('')
  .map(Number)
  .map((n, __, t) => n ** t.length)
  .reduce((a, b) => a + b) === number
