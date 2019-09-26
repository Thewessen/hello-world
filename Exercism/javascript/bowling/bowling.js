'use strict'

export class Bowling {
  constructor () {
    this.game = Bowling.start()
    this._score = this.game.next().value
  }

  static check (pins) {
    if (pins > 10) {
      throw new Error('Pin count exceeds pins on the lane')
    }
    return pins
  }

  static * start () {
    const sum = (a, b) => a + b
    const scores = []
    let bonus = 0
    for (let frame = 0; frame < 10; frame += 1) {
      let total = 0
      for (let thrw = 0; thrw < 2; thrw += 1) {
        let pins = Bowling.check(yield scores.reduce(sum, 0) + total)
        if (bonus) {
          scores[frame - 1] += pins
          bonus -= 1
        }
        if (bonus > 1) {
          scores[frame - 2] += pins
          bonus = 1
        }
        total += pins
        if (total === 10) {
          bonus += thrw % 2 ? 1 : 2
          break
        }
      } 
      scores.push(Bowling.check(total))
    }
    let pins = 0
    while (bonus > 0) {
      pins += Bowling.check(yield scores.reduce(sum))
      bonus -= 1
      if (bonus > 1) {
        scores[scores.length - 2] += pins
        bonus = 1
      }
      if (pins === 10) {
        scores[scores.length - 1] += pins
        pins = 0
      }
    }
    scores[scores.length - 1] += Bowling.check(pins)
    yield scores.reduce(sum)
  }

  roll (pins) {
    if (pins < 0) {
      throw new Error('Negative roll is invalid')
    }
    const { value, done } = this.game.next(pins)
    if (done) {
      throw new Error('Cannot roll after game is over')
    }
    this._score = value
  }

  score () {
    const { done } = this.game.next()
    if (!done) {
      throw new Error('Score cannot be taken until the end of the game')
    }
    return this._score
  }
}
