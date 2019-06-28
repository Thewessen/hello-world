'use strict'

const product = (a, b) => a * b

const slicer = (n) => (prod, __, i, nrs) => {
  if (n + i <= nrs.length) {
    const p = nrs.slice(i, n + i).reduce(product)
    if (p > prod) {
      return p
    }
  }
  return prod
}

export const largestProduct = (nr, slc) => {
  if (slc > nr.length) {
    throw new Error('Slice size is too big.')
  }
  if (slc === 0) {
    return 1
  }
  if (slc < 0 || !/^[0-9]+$/.test(nr)) {
    throw new Error('Invalid input.')
  }
  return nr
    .split('').map(Number)
    .reduce(slicer(slc), 0)
}
