'use strict'

export class Prime {
  constructor () {
  }
  
  * gen_primes () {
    yield 2
    const primes = []
    for (let n = 3; ;n += 2) {
      if (primes.every(p => n % p != 0)) {
        primes.push(n)
        yield n
      }
    }
  }

  nth (number) {
    if (!Number.isInteger(number) || number < 1) {
      throw Error('Prime is not possible')
    }
    const iter = this.gen_primes()
    for (let count = 1; count < number; count += 1) {
      iter.next()
    }
    return iter.next().value
  }
}
