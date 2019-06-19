'use strict'

const dnaError = (dna1, dna2) => {
  let l1 = dna1.length
  let l2 = dna2.length
  if (l1 === l2) {
    return
  }
  if (l1 === 0) {
    throw new Error('left strand must not be empty')
  }
  if (l2 === 0) {
    throw new Error('right strand must not be empty')
  }
  if (l1 !== l2) {
    throw new Error('left and right strands must be of equal length')
  }
}

export const compute = (dna1, dna2) => {
  try {
    dnaError(dna1, dna2)
  } catch (e) {
    throw e
  }
  return dna1
    .split('')
    .reduce((acc, curr, idx) =>
      curr !== dna2[idx]
        ? acc + 1
        : acc
    , 0)
}
