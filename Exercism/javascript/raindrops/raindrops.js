'use strict'

const dividable = (a) => (b) => a % b === 0

const SOUNDS = new Map([
  [3, 'Pling'],
  [5, 'Plang'],
  [7, 'Plong']
])

export const convert = (int) => {
  if (!Number.isInteger(int)) {
    throw new Error('convert requires an integer')
  }
  let div = dividable(int)
  let song = [...SOUNDS.keys()]
    .map((e) => div(e) ? SOUNDS.get(e) : '')
    .join('')
  return song === ''
    ? int.toString()
    : song
}
