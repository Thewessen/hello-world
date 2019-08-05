'use strict'

const count = function * (from) {
  for (let n = from; ; n += 1) {
    yield n
  }
}

const filter = function * (fn, iter) {
  for (const n of iter) {
    if (fn(n)) {
      yield n
    }
  }
}

const gen_primes = function * (till = Math.POSITIVE_INFINITY) {
  let numbers = count(2)
  while (true) {
    const p = numbers.next().value
    if (p > till) {
      break
    }
    yield p
    numbers = filter((n) => n % p, numbers)
  }
}

export const primes = (till) => {
  return [...gen_primes(till)]
}
