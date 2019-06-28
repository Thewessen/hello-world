'use strict'

export const parse = (sentence) =>
  sentence
    .toUpperCase()
    .split(/[^A-Z']/)
    .map((word) => word[0])
    .join('')
