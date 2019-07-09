'use strict'

const BITSIZE = 7

const group = (count) => (bits) => {
  const b = []
  do {
    b.unshift(lastBits(bits, count))
    bits >>>= count
  } while (bits > 0)
  return b
}

const lastBits = (byte, count) => byte & (1 << count) - 1

const eachGroup = (fn) => (group) => group.map(fn)

const setMSB = (bit) => (bits, i, group) =>
  i !== group.length - 1
    ? bits | (1 << bit - 1)
    : bits

const flatten = (arr1, arr2) => [...arr1, ...arr2]

export const encode = (bytes) =>
  bytes
    .map(group(BITSIZE))
    .map(eachGroup(setMSB(BITSIZE + 1)))
    .reduce(flatten)

export const decode = (bytes) => {
  if (bytes.slice(-1)[0] >>> BITSIZE) {
    throw new Error('Incomplete sequence')
  }
  return bytes
    .reduce((group, byte) => {
      let value = group.pop() || 0
      // shifting too far converts
      // int to signed-int?!?
      value <<= BITSIZE - 1
      value *= 2
      return byte >>> BITSIZE
        ? [...group, value + lastBits(byte, BITSIZE)]
        : [...group, value + byte, 0]
    }, [])
    .slice(0, -1)
}
