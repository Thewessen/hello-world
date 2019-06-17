'use strict'

const ADD = 'plus'
const SUB = 'minus'
const MULT = 'multiplied'
const DIV = 'divided'
const POW = 'raised'

const EOS = Symbol('End of sequence')

const isEOS = (value) => value === EOS

const OPERATIONS = new Map()
  .set(POW, (a, b) => a ** b)
  .set(MULT, (a, b) => a * b)
  .set(DIV, (a, b) => a / b)
  .set(ADD, (a, b) => a + b)
  .set(SUB, (a, b) => a - b)

const isWordChar = (char) =>
  typeof char === 'string' && /^[-a-zA-Z0-9]$/.test(char)

const getNext = (iterator) => {
  const { value, done } = iterator.next()
  return done ? EOS : value
}

const wordsG = function * (chars) {
  const iter = chars[Symbol.iterator]()
  let char
  do {
    char = getNext(iter)
    if (isWordChar(char)) {
      let word = ''
      do {
        word += char
        char = getNext(iter)
      } while (isWordChar(char))
      yield word
    }
  } while (!isEOS(char))
}

const sumG = function * (words) {
  const regex = /^(-?\d+)(?:st|nd|th|\?)?$/
  for (const word of words) {
    const match = word.match(regex)
    if (match) {
      yield Number(match[1])
    }
    if (OPERATIONS.has(word)) {
      yield word
    }
  }
}

const solver = (...operations) => function * (parts) {
  let previous
  for (const part of parts) {
    if (typeof part === 'number') {
      previous = part
    } else {
      if (operations.some((operation) => part === operation)) {
        const fn = OPERATIONS.get(part)
        previous = fn(previous, getNext(parts))
        yield previous
      } else {
        yield previous
        previous = null
        yield part
      }
    }
  }
  // Obsolete because no order for solving is needed
  // if (previous !== null) {
  //   yield previous
  // }
}

const combine = (...generators) => function * (words) {
  const iter = generators.reduce(
    (x, gen) => gen(x)
    , words)
  let value = getNext(iter)
  while (!isEOS(value)) {
    yield value
    value = getNext(iter)
  }
}

const read = combine(wordsG, sumG)

// no order for solving needed
const solve = solver(POW, MULT, DIV, ADD, SUB)

const lastEl = (array) => array[array.length - 1]

// For some reason class is needed...
class WordProblem {
  constructor (question) {
    this.problem = read(question)
  }

  answer () {
    let solution = [...solve(this.problem)]
    if (solution.length === 0) {
      throw new Error('ArgumentError')
    }
    return lastEl(solution)
  }
}

module.exports = WordProblem
