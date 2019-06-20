'use strict'

const genFactors = function * (int) {
  for (let p = 2; p <= int; p += 1) {
    while (int % p === 0) {
      int /= p
      yield p
    }
  }
}
export const primeFactors = (int) => {
  return [...genFactors(int)]
}
