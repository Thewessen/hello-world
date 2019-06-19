'use strict'

const HANDSHAKE = new Map([
  [0b1, 'wink'],
  [0b10, 'double blink'],
  [0b100, 'close your eyes'],
  [0b1000, 'jump'],
  [0b10000, Array.prototype.reverse]
])

export const secretHandshake = (int) => {
  if (isNaN(int)) {
    throw new Error('Handshake must be a number')
  }
  let result = []
  for (const bin of HANDSHAKE.keys()) {
    if (bin & int) {
      let value = HANDSHAKE.get(bin)
      result = typeof value === 'function'
                ? value.call(result)
                : [...result, value]
    }
  }
  return result
}
