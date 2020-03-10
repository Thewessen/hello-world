'use strict'

const count = function * (from) {
  while (true) {
    yield from
    from += 1
  }
}

const filter = function * (fn, iter) {
  let g = iter.next()
  while (!g.done) {
    if (fn(g.value)) yield g.value
    g = iter.next()
  }
}

const sieve = function * (iter) {
  let { value, done } = iter.next()
  while (!done) {
    yield value
    let g = filter(n => n % value, iter)
    value = g.value
    done = g.done
  }
}

const takeWhile = function * (fn, iter) {
  let g = iter.next()
  while (!g.done) {
    if (!fn(g.value)) return null
    yield g.value
    g = iter.next()
  }
}

const primes = till =>
  [...takeWhile(n => n <= till, sieve(count(2)))]

const log = iter =>  {
  let g = iter.next()
  while (!g.done) {
    console.log(g.value)
    g = iter.next()
  }
}

// console.log(primes(10))
// log(takeWhile(n => n < 10, count(2)))
log(takeWhile(n => n <= 100000, count(2)))

