'use strict'

const operations = new Map()
  .set('plus', (a, b) => a + b)
  .set('minus', (a, b) => a - b)
  .set('multiplied by', (a, b) => a * b)
  .set('divided by', (a, b) => a / b)

class WordProblem {
  constructor (question) {
    this.question = question
  }

  answer () {
  }
}
