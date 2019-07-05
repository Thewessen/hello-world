'use strict'

const strRange = function* (from, too) {
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

const take = function * (n, iter) {
  for (let i = 0; i < n; i += 1) {
    const { value, done } = iter.next()
    if (done) {
      break
    }
    yield value
  }
}

const shuffle = function * (iter) {
  let values = [...take(rInt(1, 3), iter)].reverse()
  while (values.length > 0) {
    yield * values
    values = [...take(rInt(1, 3), iter)].reverse()
  }
}

const combine = (gen1, gen2) =>
  function * () {
    for (const v1 of shuffle(gen1())) {
      for (const v2 of shuffle(gen2())) {
        yield v1 + v2
      }
    }
  }

// const compose = (...gens) =>
//   gens.reduce((f, g) => combine(f, g))

const combine = (gen) => (chars) => function * () {
  let iters = chars.map(function* (char) {
    for (const value of gen()) {
      yield value + char
    }
  })
  let items = iters.map((iter) => iter.next().value)
  while (items.length > 0) {
    const i = rInt(0, items.length)
    yield items[i]
    const { value, done } = iters[i].next()
    if (done) {
      iters = iters.filter((__, idx) => idx !== i)
      items = items.filter((__, idx) => idx !== i)
    } else {
      items[i] = value
    }
  }
}

// const combine = function * (char, iter) {
//   for (const value of iter) {
//     yield char + value
//   }
// } 

const uniqueName = (...template) =>
  template.reduce(
    (acc, curr) => unique(acc)(curr)
  , function* () { yield ''})

module.exports = uniqueName(...TEMPLATE)
// const uniqueName = 
//   unique(
//     unique(
//       unique(
//         unique(
//           unique(function* () { yield '' })([...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
//         )([...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
//       )([...'0123456789'])
//     )([...'0123456789'])
//   )([...'0123456789'])

// module.exports = uniqueName
// module.exports = compose(
//   strRange('A', 'Z'),
//   strRange('A', 'Z'),
//   strRange('0', '9'),
//   strRange('0', '9'),
//   strRange('0', '9')
// )()

const uniqueNameGenerator = function * (template) {
  const shadow = new Map()
  const available = nCr(template)
  const combiCount = template
    .map((__, i, arr) => nCr(arr.slice(i + 1)))
  while (shadow.get('') !== available) {
    let name = ''
    for (const [idx, chars] of template.entries()) {
      if (shadow.has(name)) {
        let count = shadow.get(name)
        let char = rPick(
          chars.filter((char) =>
            !shadow.has(name + char) ||
            !(shadow.get(name + char) === combiCount[idx])
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

class Robot {
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

// module.exports = Robot

// const uniqueName = compose(
//   strRange('A', 'Z'),
//   strRange('A', 'Z'),
//   strRange('0', '9'),
//   strRange('0', '9'),
//   strRange('0', '9')
// )

// Robot._names_generator = uniqueName(...TEMPLATE)
// Robot.releaseNames = () => { Robot._names_generator = uniqueName(...TEMPLATE) }

// Robot._names_generator = uniqueNameGenerator(TEMPLATE)
// Robot.releaseNames = () => { Robot._names_generator = uniqueNameGenerator(TEMPLATE) }
