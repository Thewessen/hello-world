'use strict'

const COLORS = new Map([
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white'
].map((e, i) => [e, i]))

const value = colors => Number(colors
  .map(COLORS.get.bind(COLORS)).join(''))

export {
  value,
  COLORS
}
