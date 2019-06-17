'use strict'

const numbersTill = function * (till) {
  for (let i = 2; i <= till; i += 1) {
    yield i
  }
}

const multiplesOff = function * (number, till) {
  for (let i = 2; number * i <= till; i += 1) {
    yield number * i
  }
}

export const primes = (till) => {
  let primes = [...numbersTill(till)]
  for (let i = 0; i < primes.length; i += 1) {
    let multiples = [...multiplesOff(primes[i], till)]
    primes = primes.filter((e) => !multiples.includes(e))
  }
  return primes
}
