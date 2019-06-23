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

const uniqueName = (template) => {
  if (template.length > 0) {
    const [chars, ...rest] = template
    return rPick(chars) + uniqueName(rest)
  }
  return ''
}

const rInt = (from, too) =>
  Math.floor((Math.random() * (too - from) + from))

const rPick = (array) =>
  array[rInt(0, array.length)]

const nCr = (collection) =>
  collection.reduce((total, set) => total * set.length, 1)

const buildShadow = (name, shadow, possible, template) => {
  for (let i = 0; i < name.length; i += 1) {
    const part = name.slice(0, i + 1)
    if (shadow.has(part)) {
      let count = shadow.get(part)
      if (count + 1 === possible.get(i)) {
        let chars = template[i]
        let idx = chars.indexOf(name[i])
        template[i] = [...chars.slice(0, idx), ...chars.slice(idx + 1)]
      }
      shadow.set(part, count + 1)
    } else {
      shadow.set(part, 1)
    }
  }
  return { template, shadow }
}

// Some optimization added for passing last test
const uniqueNameGenerator = function * (template) {
  const shadow = new Map()
  const available = nCr(template)
  const combiCount = template
    .map((__, i, arr) => nCr(arr.slice(i + 1)))
  while (shadow.get('') !== available) {
    // let name = uniqueName(template)
    // for (const [i, char] of name.split('').entries()) {
    //   console.log(shadow.get(name.slice(0, i)))
    // }
    // yield name
    // for (const [i, char] of name.split('').entries()) {
    //   const part = name.slice(0, i + 1)
    //   if (shadow.has(part)) {
    //     const count = shadow.get(part)
    //     console.log(shadow.get(part))
    //     shadow.set(part, count + 1)
    //     console.log(shadow.get(part))
    //     if (count + 1 === combiCount[i]) {
    //       const chars = template[i]
    //       const idx = chars.indexOf(char)
    //       template[i] = [...chars.slice(0, idx), ...chars.slice(idx + 1)]
    //     }
    //   } else {
    //     shadow.set(part, 1)
    //   }
    // }
    // console.log(combiCount)
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

export class Robot {
// class Robot {
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

Robot._names_generator = uniqueNameGenerator(TEMPLATE)
Robot.releaseNames = () => { Robot._names_generator = uniqueNameGenerator(TEMPLATE) }
