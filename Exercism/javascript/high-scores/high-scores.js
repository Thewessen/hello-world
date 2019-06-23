'use strict'

export class HighScores {
  constructor (scores) {
    this._scores = scores
  }

  get scores() {
    return this._scores
  }

  get latest() {
    return this._scores.slice(-1)[0]
  }

  get personalBest() {
    return this._scores
      .reduce((a, b) => a > b ? a : b)
  }

  get personalTopThree() {
    return [...this._scores]
      .sort((a, b) => b - a)
      .slice(0, 3)
  }
}
