'use strict'

// Given a number, find the sum of all the unique multiples of particular numbers up to but not including that number.

// If we list all the natural numbers below 20 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.

// The sum of these multiples is 78.

module.exports = (mutiples, till) => mutiples
  .filter((i) => Number.isInteger(i))
  .filter((i) => i < till)
  .reduce((acc, curr) => {
    for (let i = 1; curr * i < till; i += 1) {
      if (!acc.includes(curr * i)) {
        acc.push(curr * i)
      }
    }
    return acc
  }, [0])
  .reduce((acc, curr) => acc + curr)
