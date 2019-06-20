'use strict'

const numbers = function * (till) {
  for (let i = 1; i < till + 1; i += 1) {
    yield i
  }
}

const isDividerOf = (a) => (b) => a % b === 0

const aliquotSum = (isDivider) => (int) =>
  [...numbers(parseInt(int / 2))]
  .filter(isDivider)
  .reduce((a, b) => a + b, 0)

const perfect = (aliquot, int) => aliquot === int
const abundant = (aliquot, int) => aliquot > int
const deficient = (aliquot, int) => aliquot < int

const matchType = (int) => (aliSum) => (fn) => fn(aliSum(int), int)

const fnName = (__, fn) => fn.name

const combine = (...fns) => (int) => fns.reduce((int, fn) => fn(int), int)

export const classify = (int) => {
  if(!Number.isInteger(int) || int <= 0) {
    throw new Error('Classification is only possible for natural numbers.')
  }
  return [perfect, abundant, deficient]
    .filter(
      combine(
        isDividerOf,
        aliquotSum,
        matchType(int)
      )(int)
    ).reduce(fnName, '')
}
