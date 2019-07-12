'use strict'

const words = /[A-Z]+/g
const chars = /[A-Z]/g
const letters = (str) => Array.from(new Set(str.match(chars)))
const firstLetters = (str) => new Set(str.replace(words, (w) => w[0]))
const numbers = (from, to) => Array.from(
  { length: to - from + 1 },
  (__, i) => i + from
)

const solutionGen = function* (letters, scores, notZero, result) {
  result = result || {}
  notZero = notZero || new Set()
  const letter = letters.pop()
  const scrs = notZero.has(letter)
    ? scores.filter((n) => n !== 0)
    : scores
  for (const score of scrs) {
    result[letter] = score
    if (letters.length === 0) {
      yield result
    } else {
      yield* solutionGen(
        [...letters],
        scores.filter((s) => s !== score),
        notZero,
        result
      )
    }
  }
}

export const solve = (puzzle) => {
  let solution = null
  for (const sol of solutionGen(
    letters(puzzle),
    numbers(0, 9),
    firstLetters(puzzle)
  )) {
    if (eval(puzzle.replace(chars, (char) => sol[char]))) {
      if (solution) {
        return null
      }
      solution = { ...sol }
    }
  }
  return solution
}
