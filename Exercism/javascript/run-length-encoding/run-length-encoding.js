'use strict'

export const encode = (string) => string === '' ? string : string
  .match(/(.)\1*/g)
  .reduce((acc, curr) => [...acc, curr.length === 1 ? '' : curr.length, curr[0]], [])
  .join('')

export const decode = (string) => string === '' ? string : string
  .match(/(\d+)?./g)
  .map(e => e[e.length - 1].repeat(isNaN(parseInt(e)) ? 1 : parseInt(e)))
  .join('')
