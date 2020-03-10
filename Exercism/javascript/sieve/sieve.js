'use strict'

const count = function * (from) {
  while (true) {
    yield from
    from += 1
  }
}

const sieve = function * (numbers) {
  const filters = []

  while (true) {
    const { value: p } = numbers.next()

    if (filters.some(f => f(p))) continue

    yield p
    filters.push(n => n % p === 0)
  }
}

const takeWhile = function * (fn, iter) {
  let g = iter.next()
  while (!g.done) {
    if (!fn(g.value)) return
    yield g.value
    g = iter.next()
  }
}

export const primes = till =>
  [...takeWhile(n => n <= till, sieve(count(2)))]

// const log = iter => {
//   while (true) {
//     const { value, done } = iter.next()
//     if (done) break
//     console.log(value)
//   }
// }

// log(sieve(count(2)))
