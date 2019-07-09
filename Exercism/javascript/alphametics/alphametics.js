'use strict'

const letters = (str) => new Set(str.match(/[A-Z]/g))
const words = (str) => str.match(/[A-Z]+/g)

const combine = function* (letter, scores) {
  for (const score of scores) {
    yield [letter, score]
  }
}

const solutionGen = function* (letters, scores, solution = {}) {
  const letter = letters.pop()
  for (const score of scores) {
    solution[letter] = score
    console.log(solution)
    if (letters.length === 0) {
      yield solution
    } else {
      yield* solutionGen(letters, scores.filter((s) => s !== score), solution)
      yield solution
    }
  }
}

module.exports = solutionGen

const solve = (puzzle) => {
  const l = letters(puzzle)
}
