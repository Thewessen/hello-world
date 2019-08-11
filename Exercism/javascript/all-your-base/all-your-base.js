'use strict'

export const convert = (digits, currBase, convBase) => {
  if (!Number.isInteger(currBase) || currBase <= 1) {
    throw new Error('Wrong input base')
  }
  if (!Number.isInteger(convBase) || convBase <= 1) {
    throw new Error('Wrong output base')
  }
  if ((digits[0] === 0 && digits.length > 1)
      || digits.length === 0
      || digits.some(d => d < 0)
      || digits.some(d => d >= currBase)) {
    throw new Error('Input has wrong format')
  }
  let value = digits
    .reverse()
    .map((n, i) => n * (currBase ** i))
    .reduce((a, b) => a + b)
  return value === 0
    ? [0]
    : [...(function * (value, base) {
        for (; value !== 0; value = ~~(value / base)) {
          yield value % base
        }
      })(value, convBase)]
     .reverse()
}
