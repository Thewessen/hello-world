'use strict'

export const proverb = (...items) => {
  let rhyme = ''
  let qualifier = ''
  for (let i = 0; i < items.length - 1; i += 1) {
    if (typeof items[i + 1] === 'object') {
      qualifier = items[i + 1].qualifier + ' '
      break
    }
    rhyme += `For want of a ${items[i]} the ${items[i + 1]} was lost.\n`
  }
  return rhyme + `And all for the want of a ${qualifier}${items[0]}.`
}
