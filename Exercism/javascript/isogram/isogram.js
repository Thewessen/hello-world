'use strict'

export const isIsogram = (word) => !/([a-z]).*\1/.test(word.toLowerCase())
