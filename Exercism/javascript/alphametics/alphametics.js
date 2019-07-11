'use strict'

const words = /[A-Z]+/g
const chars = /[A-Z]/g
const letters = (str) => Array.from(new Set(str.match(chars)))
const firstLetters = (str) => new Set(str.replace(words, (w) => w[0]))
const numbers = (to) => Array.from({ length: to }, (__, i) => i)

const solutionGen = function* (letters, scores, notZero, solution) {
  notZero = notZero || new Set()
  solution = solution || {}
  const letter = letters.pop()
  const scrs = notZero.has(letter) ? scores.filter((s) => s !== 0) : scores
  for (const score of scrs) {
    solution[letter] = score
    if (letters.length === 0) {
      yield solution
    } else {
      yield* solutionGen(
        [...letters],
        scores.filter((s) => s !== score),
        notZero,
        solution
      )
    }
  }
}

export const solve = (puzzle) => {
  const lets = letters(puzzle)
  const scrs = numbers(10)
  const notZero = firstLetters(puzzle)
  let solution = null
  for (const sol of solutionGen(lets, scrs, notZero)) {
    if (eval(puzzle.replace(chars, (char) => sol[char]))) {
      if (solution) {
        return null
      }
      solution = { ...sol }
    }
  }
  return solution
}
