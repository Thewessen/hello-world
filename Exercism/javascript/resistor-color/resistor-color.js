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

export const colorCode = (color = '') => COLORS.get(color.toLowerCase())
