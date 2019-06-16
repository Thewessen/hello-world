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

export const value = (colors) => Number.parseInt(
  colors.reduce(
    (acc, curr) => acc + COLORS.get(curr.toLowerCase()).toString(),
    ''
  ))
