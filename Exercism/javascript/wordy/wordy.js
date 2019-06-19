'use strict'

const ADD = 'plus'
const SUB = 'minus'
const MULT = 'multiplied'
const DIV = 'divided'
const POW = 'raised'

const OPERATIONS = new Map()
  .set(POW, (a) => (b) => a ** b)
  .set(MULT, (a) => (b) => a * b)
  .set(DIV, (a) => (b) => a / b)
  .set(ADD, (a) => (b) => a + b)
  .set(SUB, (a) => (b) => a - b)

// Anonymous arrowfunc (we use here) have different this binding!
// const isFunction = (obj) => Object.prototype.toString.call(obj) === '[object Function]'

// Less secure, but works for this example
const isFunction = (obj) => typeof obj === 'function'

const isNumber = (word) => /^(-?\d+)(?:st|nd|th|\?)?$/.test(word)
const grepNumber = (word) => Number.parseFloat(word)

const isProblem = (word) => OPERATIONS.has(word) || isNumber(word)
const transformType = (word) => OPERATIONS.has(word) ? OPERATIONS.get(word) : grepNumber(word)

const solve = (acc, curr) => {
  if (isFunction(acc) ? isFunction(curr) : !isFunction(curr)) {
    throw new Error('Unsolvable')
  }
  if (isFunction(curr)) {
    return curr(acc)
  }
  if (typeof curr === 'number') {
    return acc(curr)
  }
}

// For some reason class is needed...
export class WordProblem {
  constructor (question) {
    this.problem = question
      .split(' ')
      .filter(isProblem)
      .map(transformType)
  }

  answer () {
    if (this.problem.length < 2) {
      throw new Error('Not much to solve!')
    }
    try {
      return this.problem.reduce(solve)
    } catch(e) {
      throw e
    }
  }
}

// module.exports = WordProblem
