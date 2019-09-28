'use strict'

const FRAMECOUNT = 10
const THROWCOUNT = 2
const PINCOUNT = 10
const sum = (arr) => arr.reduce((a, b) => a + b, 0)
const total = (scores) => sum(scores.map((f) => f.score))

export class Frame {
  constructor() {
    this._rolls = []
    this.bonus = 0
    this._score = 0
  }

  get score() {
    return this._score
  }

  set score(value) {
    this._score = sum(this.rolls) + value
  }

  set rolls(pins) {
    this._rolls = [...this._rolls, pins]
  }
  
  get rolls() {
    return this._rolls
  }

  check() {
    const check = this.rolls.length === THROWCOUNT
      && this.score <= PINCOUNT
    if ((this.rolls.length === THROWCOUNT
        && this.score <= PINCOUNT)
      || (this.rolls.length === THROWCOUNT + 1() {
      throw new Error('Pin count exceeds pins on the lane')
    }
  }
  // reset() {
  //   this.pins = PINCOUNT
  // }
}

export class Bowling {
  constructor () {
    this.game = Bowling.start()
    Object.assign(this, this.game.next())
  }

  static check (pins) {
    if (pins > PINCOUNT) {
      throw new Error('Pin count exceeds pins on the lane')
    }
    return pins
  }

  static * rolls (frame, total) {
    if (frame.rolls.length === THROWCOUNT) {
      return frame
    }
    frame.rolls = yield total + frame.score
    frame.check()
    if (frame.score === PINCOUNT) {
      frame.bonus = frame.rolls.length % 2 ? 2 : 1
      return frame
    }
    return yield * Bowling.rolls(frame, total)
  }

  static * frames (scores, bonus) {
    if(scores.length === FRAMECOUNT) {
      return scores
    }
    const frame = yield * Bowling.rolls(new Frame(), total(scores))
    let bonusFrames = scores.filter(frame => frame.bonus)
    for (const roll of frame.rolls) {
      bonusFrames = bonusFrames.map(frame => {
        frame.rolls = roll
        frame.bonus -= 1
        return frame
      }).filter(frame => frame.bonus)
    }
    return yield * Bowling.frames([...scores, frame], bonus)
  }

  static * start () {
    // Regular frames
    let scores = yield * Bowling.frames([], 0)
    console.log(scores)

    // Fill balls
    let bonusFrames = scores.filter(frame => frame.bonus)
    let pins = 0
    for (let i = 0; i < 2 && bonusFrames.length > 0; i += 1) {
      let roll = yield total(scores)
      Bowling.check(pins += roll)
      bonusFrames = bonusFrames.map(frame => {
        frame.rolls = pins
        frame.bonus -= 1
        console.log(frame)
        return frame
      }).filter(frame => frame.bonus)
      if (pins === PINCOUNT) {
        pins = 0
      }
    }
    return total(scores)
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
