'use strict'

const enhance = (coin) => (change, total, solutions) => {
  if (coin === total) {
    solutions[total] = [coin]
  } else if (coin < total) {
    if (change && solutions[total - coin]) {
      solutions[total] = change.length < (1 + solutions[total - coin].length)
        ? change
        : [...solutions[total - coin], coin]
    } else if (solutions[total - coin]) {
      solutions[total] = [...solutions[total - coin], coin]
    }
  }
}

export class Change {
  calculate(currency, total) {
    if (total === 0) {
      return []
    }
    if (total < 0) {
      throw new Error('Negative totals are not allowed.')
    }
    const solutions = Array(total + 1).fill(null)
    for (const coin of currency.filter(c => c <= total)) {
      solutions.forEach(enhance(coin))
    }
    const result = solutions.slice(-1)[0]
    if (result === null) {
      throw new Error(`The total ${total} cannot be represented in the given currency.`)
    }
    return result
  }
}
