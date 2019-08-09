'use strict'

export const keep = (arr, fn) => arr.filter(fn)

export const discard = (arr, fn) => arr.filter(e => !fn(e))
