'use strict'

const strRange = function * (from, too) {
  const [start, end] = [from, too]
    .map((e, i) => e.charCodeAt() + i)
  for (let code = start; code < end; code += 1) {
    yield String.fromCharCode(code)
  }
}

const TEMPLATE = [
  [...strRange('A', 'Z')],
  [...strRange('A', 'Z')],
  [...strRange('0', '9')],
  [...strRange('0', '9')],
  [...strRange('0', '9')]
]

const rInt = (from, too) =>
  Math.floor((Math.random() * (too - from) + from))

const rPick = (array) =>
  array[rInt(0, array.length)]

const nCr = (collection) =>
  collection.reduce((total, set) => total * set.length, 1)

// Some optimization added for passing last test
const uniqueNameGenerator = function * (template) {
  const shadow = new Map()
  const available = nCr(template)
  const combiCount = new Map(
    template.map((e, i, arr) =>
      nCr(arr.slice(i + 1))).entries()
  )
  while (shadow.get('') !== available) {
    let name = ''
    for (const [idx, chars] of template.entries()) {
      if (shadow.has(name)) {
        let count = shadow.get(name)
        let char = rPick(
          chars.filter((char) =>
            !shadow.has(name + char) ||
            !(shadow.get(name + char) === combiCount.get(idx))
          )
        )
        shadow.set(name, count + 1)
        name += char
      } else {
        let char = rPick(chars)
        shadow.set(name, 1)
        name += char
      }
    }
    shadow.set(name, 1)
    yield name
  }
}

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
    const { value, done } = Robot._names_generator.next()
    if (done) {
      throw new Error('No more Robots for you!')
    }
    this._name = value
  }
}

Robot._names_generator = uniqueNameGenerator(TEMPLATE)
Robot.releaseNames = () => { Robot._names_generator = uniqueNameGenerator(TEMPLATE) }
