'use strict'

export const sumOfMultiples = (mutiples, till) => mutiples
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
