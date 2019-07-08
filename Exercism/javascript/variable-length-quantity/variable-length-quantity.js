'use strict'

const group = (count) => (bits) => {
  const b = []
  do {
    b.unshift(bits & (2 ** count - 1))
    bits >>>= count
  } while (bits > 0)
  return b
}

const eachGroup = (fn) => (group) => group.map(fn)

const setMSB = (bit) => (bits, i, group) =>
  i !== group.length - 1
    ? bits + 2 ** (bit - 1)
    : bits

const flatten = (arr1, arr2) => [...arr1, ...arr2]

export const encode = (bytes) =>
  bytes
    .map(group(7))
    .map(eachGroup(setMSB(8)))
    .reduce(flatten)

export const decode = (bytes) => {
  if (bytes.slice(-1)[0] >= 2 ** 7) {
    throw new Error('Incomplete sequence')
  }
  return bytes
    .reduce((group, byte) => {
      let value = group.pop() || 0
      // shifting too far converts
      // int to signed-int?!?
      value <<= 6
      value *= 2
      return byte >= 2 ** 7
        ? [...group, value + byte - 2 ** 7]
        : [...group, value + byte, 0]
    }, [])
    .slice(0, -1)
}
