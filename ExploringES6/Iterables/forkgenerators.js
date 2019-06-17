'use strict'

// An self created example forking generators together...
// this is actually unused code from an Exercism.io exercise

const add = (a, b) => a + b
const sub = (a, b) => a - b
const mult = (a, b) => a * b
const div = (a, b) => a / b

const OPERATIONS = new Map()
  .set('minus', sub)
  .set('plus', add)
  .set('divided', div)
  .set('multiplied', mult)

const EOS = Symbol('End of sequence')

const isEOS = (value) => value === EOS

const isWordChar = (char) =>
  typeof char === 'string' && /^[a-zA-Z0-9]$/.test(char)

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

const numbersG = function * (words) {
  const regex = /^([0-9]+)(?:st|nd|th)?$/
  for (const word of words) {
    const match = word.match(regex)
    if (match) {
      yield Number(match[1])
    }
  }
}

const operationsG = function * (words) {
  for (const word of words) {
    if (OPERATIONS.has(word)) {
      yield OPERATIONS.get(word)
    }
  }
}

const fork = (firstgen, ...nextgens) => {
  return function * (words) {
    const iters = nextgens.map(
      (gen) => gen(firstgen(words))
    )
    let values = iters.map(
      (iter) => getNext(iter)
    )
    while (!values.every(isEOS)) {
      yield values
      values = iters.map(
        (iter) => getNext(iter)
      )
    }
  }
}

const read = fork(wordsG, numbersG, operationsG)

module.exports = read
