'use strict'

const KEY_SIZE = 137
const BASEINT = 'a'.charCodeAt()

const chars = function * (from, too) {
  const start = from.charCodeAt()
  const end = too.charCodeAt() + 1
  for (let code = start; code < end; code += 1) {
    yield String.fromCharCode(code)
  }
}

const take = function * (int, generator) {
  const iter = generator()
  for (let t = 0; t < int; t += 1) {
    yield iter.next().value
  }
  iter.return()
}

const randomInt = (from, till) =>
  Math.floor((Math.random() * (till - from) + from))

const genRandomChars = function * () {
  const alph = [...chars('a', 'z')]
  while (true) {
    yield alph[randomInt(0, alph.length)]
  }
}

const randomKey = (size) => [...take(size, genRandomChars)]

const charToInt = (char) => char.toLowerCase().charCodeAt()

const reBase = (baseInt) => (charCode) => charCode - baseInt

const rot = (key) => (charInt, index) => (charInt + key[index % key.length]) % 26

const intToChar = (charInt) => String.fromCharCode(charInt)

export class Cipher {
  constructor (key) {
    if (typeof key !== 'undefined' && !/^[a-z]+$/.test(key)) {
      throw new Error('Bad key')
    }
    this._key = key ? Array.from(key) : randomKey(KEY_SIZE)
  }

  encode (string) {
    let key = this._key
      .map(charToInt)
      .map(reBase(BASEINT))

    return string
      .split('')
      .map(charToInt)
      .map(reBase(BASEINT))
      .map(rot(key))
      .map(reBase(-BASEINT))
      .map(intToChar)
      .join('')
  }

  decode (string) {
    let key = this._key
      .map(charToInt)
      .map(reBase(BASEINT))
      .map((i) => 26 - i)

    return string
      .split('')
      .map(charToInt)
      .map(reBase(BASEINT))
      .map(rot(key))
      .map(reBase(-BASEINT))
      .map(intToChar)
      .join('')
  }

  get key () {
    return this._key.join('')
  }
}
