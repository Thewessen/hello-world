'use strict'

const FRAMECOUNT = 10
const THROWCOUNT = 2
const PINSCOUNT = 10
const sum = (a, b) => a + b

class Frame {
  constructor(throws = THROWCOUNT, bonusFrame = false) {
    this._throws = throws
    this.bonusFrame = bonusFrame
    this._pins = PINSCOUNT
    this.score = 0
  }

  set pins(value) {
    if(value < 0) {
      throw new Error('Pin count exceeds pins on the lane')
    }
    if(this._throws === 0) {
      throw new Error('Cannot throw after frame is over')
    }
    this._throws -= 1
    this.score = PINSCOUNT - value
    this._pins = value
  }

  get pins() {
    return this._pins
  }
}

export class Bowling {
  constructor () {
    this.game = Bowling.start()
    Object.assign(this, this.game.next())
  }

  static check (pins) {
    if (pins > 10) {
      throw new Error('Pin count exceeds pins on the lane')
    }
    return pins
  }

  static * frames (scores, bonus) {
    if(scores.length === FRAMECOUNT) {
      return [ scores, bonus ]
    }
    let total = 0
    for (let thrw = 0; thrw < THROWCOUNT; thrw += 1) {
      const pins = yield scores.reduce(sum, 0) + total
      Bowling.check(total += pins)
      if (bonus) {
        scores[scores.length - 1] += pins
        bonus -= 1
      }
      if (bonus > 1) {
        scores[scores.length - 2] += pins
        bonus = 1
      }
      if (total === 10) {
        bonus += thrw % 2 ? 1 : 2
        break
      }
    } 
    return yield * Bowling.frames([...scores, total], bonus)
  }

  static * start () {
    // Regular frames
    let [ scores, bonus ] = yield * Bowling.frames([], 0)

    // Fill balls
    let pins = 0
    while (bonus > 0) {
      Bowling.check(pins += yield scores.reduce(sum))
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
    scores[scores.length - 1] += pins
    return scores.reduce(sum)
  }

  roll (pins) {
    if (this.done) {
      throw new Error('Cannot roll after game is over')
    }
    if (pins < 0) {
      throw new Error('Negative roll is invalid')
    }
    Object.assign(this, this.game.next(pins))
  }

  score () {
    if (!this.done) {
      throw new Error('Score cannot be taken until the end of the game')
    }
    return this.value
  }
}
