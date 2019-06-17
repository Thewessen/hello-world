'use strict'

const TOTAL_NUMBER_OF_NAMES = (
    26 // A-Z
  * 26 // A-Z
  * 10 // 0-9
  * 10 // 0-9
  * 10 // 0-9
)

const randomInt = (from, too) =>
  Math.floor((Math.random() * (too - from) + from))

const randomPick = (array) =>
  array[randomInt(0, array.length)]

const chars = function * (from, too) {
  const start = from.charCodeAt()
  const end = too.charCodeAt() + 1
  for (let code = start; code < end; code += 1) {
    yield String.fromCharCode(code)
  }
}

const numbers = function * (from, too) {
  for (let i = from; i <= too; i += 1) {
    yield i
  }
}

const randomName = (...arrays) => {
  let name = ''
  for (const array of arrays) {
    name += randomPick(array)
  }
  return name
}

export class Robot {
  constructor () {
    this._name = this.generateName()
  }

  reset () {
    this._name = this.generateName()
  }

  get name () {
    return this._name
  }

  generateName () {
    if (Robot.USED.size === TOTAL_NUMBER_OF_NAMES) {
      throw new Error('No more Robots for you!')
    }
    let name
    do {
      name = randomName(
        [...chars('A','Z')],
        [...chars('A','Z')],
        [...numbers(1, 9)],
        [...numbers(0, 9)],
        [...numbers(0, 9)]
      )
    } while (Robot.USED.has(name))
    Robot.USED.add(name)
    return name
  }
}

Robot.USED = new Set()
Robot.releaseNames = () => Robot.USED.clear()
