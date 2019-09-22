'use strict'

const randomInt = (from, too) => Math.floor((Math.random() * (too - from) + from))
const randomPick = (array) => array[randomInt(0, array.length)]

const chars = function * (from, too) {
  for (let code = from.charCodeAt(); code <= too.charCodeAt(); code += 1) {
    yield String.fromCharCode(code)
  }
}

const numbers = function * (from, too) {
  for (let i = from; i <= too; i += 1) {
    yield i
  }
}

const randomName = (...args) => {
  let name = ''
  for (const array of args) {
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
    let name
    do {
      name = randomName(
        [...chars('A', 'Z')],
        [...chars('A', 'Z')],
        [...numbers(0, 9)],
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
