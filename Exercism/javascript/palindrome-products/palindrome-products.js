'use strict'

const isPalindrome = (n) => n
  .toString()
  .split('')
  .reverse()
  .join() === n.toString()

const genPalindrom = function * (from, too) {
  for (let a = from; a < too; a += 1) {
    for (let b = a; b < too; b += 1) {
      if(isPalindrome(a * b)) {
        yield [a, b]
      }
    }
  }
}

export class Palindromes {
  static generate ({ maxFactor, minFactor = 1}) {
    if (minFactor > maxFactor) {
      throw new Error('min must be <= max')
    }
    const factors = [...genPalindrom(minFactor, maxFactor)]
    this.smallest = {
      value: factors[0].reduce((a, b) => a * b),
      factors: factors[0]
    }
    this.largest = {
      value: factors.splice(-1).reduce((a, b) => a * b),
      factors: factors.splice(-1)
    }

  }
}
