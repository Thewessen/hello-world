'use strict'

class Bucket {
  constructor (size) {
    this.size = size
    this._value = 0
  }

  get value() {
    return this._value
  }

  set value (value) {
    this._value = value < 0
      ? 0
      : value > this.size
        ? this.size
        : value
  }

  empty () {
    this.value = 0
  }

  fill () {
    this.value = this.size
  }

  isFull () {
    return this.value === this.size
  }

  isEmpty() {
    return this.value === 0
  }

  leftOver() {
    return this.size - this.value
  }

  pour (bucket) {
    const diff = bucket.leftOver()
    bucket.value += this.value
    this.value -= diff
  }
}

export class TwoBucket {
  constructor (buckOne, buckTwo, goal, starterBuck) {
    this.start = starterBuck
    this.other = starterBuck === 'one' ? 'two' : 'one'
    this.goal = goal
    this.one = new Bucket(buckOne)
    this.two = new Bucket(buckTwo)
  }

  moves() {
    const { start, other, goal } = this
    const bck1 = this[start]
    const bck2 = this[other]
    if (bck1.value === goal) {
      return 0
    }
    if (bck2.isFull()) {
      bck2.empty()
      return 1 + this.moves()
    }
    if (bck1.isEmpty()) {
      bck1.fill()
      return 1 + this.moves()
    }
    bck1.pour(bck2)
    return 1 + this.moves()
  }

  get goalBucket() {
    return this.start
  }

  get otherBucket() {
    return this[this.other].value
  }
}
