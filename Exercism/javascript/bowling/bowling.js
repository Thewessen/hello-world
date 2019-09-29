'use strict'

const FRAMECOUNT = 10
const THROWCOUNT = 2
const PINCOUNT = 10
const sum = (arr) => arr.reduce((a, b) => a + b, 0)
const total = (scores) => sum(scores.map((f) => f.score))

export class Frame {
  constructor() {
    this.pins = PINCOUNT
    this._rolls = []
    this.bonus = 0
    this.last = false
  }

  get score() {
    return sum(this.rolls)
  }

  get rolls() {
    return this._rolls
  }

  roll(pins) {
    this.pins -= pins
    if (this.pins < 0) {
      throw new Error('Pin count exceeds pins on the lane')
    }
    if (this.last && !this.pins) {
      this.pins = PINCOUNT
    }
    this._rolls.push(pins)
  }
  
  addBonus(pins) {
    if (this.bonus) {
      this.rolls.push(pins)
      this.bonus -= 1
    }
  }

  setLast() {
    this.last = true
    this.pins = PINCOUNT
    return this
  }

  * play (total) {
    if (this.rolls.length === THROWCOUNT) {
      return this
    }
    this.roll(yield total + this.score)
    if (this.score === PINCOUNT) {
      this.bonus = this.rolls.length % 2 ? 2 : 1
      return this
    }
    return yield * this.play(total)
  }
}

export class Bowling {
  constructor () {
    this.game = Bowling.play()
    Object.assign(this, this.game.next())
  }

  static * frames (scores, bonus) {
    if(scores.length === FRAMECOUNT) {
      return scores
    }
    const frame = yield * new Frame().play(total(scores))
    for (const roll of frame.rolls) {
      scores.forEach(frame => frame.addBonus(roll))
    }
    return yield * Bowling.frames([...scores, frame], bonus)
  }

  static * play () {
    // Regular frames
    const scores = yield * Bowling.frames([], 0)

    // Last frame
    const lastFrame = scores.pop().setLast()
    if (lastFrame.rolls.length < 2) {
      const pins = yield total([...scores, lastFrame])
      lastFrame.roll(pins)
      scores.forEach(frame => frame.addBonus(pins))
    }

    // fillball
    if ([...scores, lastFrame].some(frame => frame.bonus)) {
      lastFrame.roll(yield total([...scores, lastFrame]))
    }
    return total([...scores, lastFrame])
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
