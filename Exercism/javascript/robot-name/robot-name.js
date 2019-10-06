'use strict'

const strArray = (from, too) => {
  const [start, end] = [from, too]
    .map((e, i) => String(e).charCodeAt() + i)
  return Array.from(
    { length: end - start },
    (__, i) => String.fromCharCode(start + i)
  )
}

const rInt = (from, to) =>
  Math.floor((Math.random() * (to - from) + from))

const prepend = (genNames) => function * (char) {
  for (const name of genNames()) {
    yield name + char
  }
}

const combine = (gen, chars) => function * () {
  let iters = chars.map(prepend(gen))
  let values = iters.map((iter) => iter.next().value)
  while (values.length > 0) {
    const i = rInt(0, values.length)
    yield values[i]
    const { value, done } = iters[i].next()
    if (done) {
      iters.splice(i, 1)
      values.splice(i, 1)
    } else {
      values[i] = value
    }
  }
}

const uniqueNames = (...template) =>
  template.reduce(combine,
    function* () { yield '' })()

export class Robot {
  constructor () {
    this.generateName()
  }

  reset () {
    this.generateName()
  }

  get name () {
    return this._name
  }

  generateName () {
    const { value, done } = Robot.uniqueNames.next()
    if (done) {
      throw new Error('No more Robots for you!')
    }
    this._name = value
  }

  static releaseNames() {
    Robot.uniqueNames = uniqueNames(...Robot.template)
  }
}

Robot.template = [
    strArray('A', 'Z'),
    strArray('A', 'Z'),
    strArray('0', '9'),
    strArray('0', '9'),
    strArray('0', '9')
  ]

Robot.releaseNames()
