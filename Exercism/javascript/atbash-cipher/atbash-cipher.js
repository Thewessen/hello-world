'use strict'

const LOWERCASE_ALPHA = Array.from(
  { length: 26 }, (__, i) =>
  String.fromCharCode(i + 'a'.charCodeAt())
)

const TRANSLATION = new Map(
  (function * (arr1, arr2) {
    for (const [index, char] of arr1.entries()) {
      yield [char, arr2[index]]
    }
  })(LOWERCASE_ALPHA, [...LOWERCASE_ALPHA].reverse())
)

export const encode = (string) => string
  .toLowerCase()
  .replace(/\W/g, '')
  .replace(/\D/g, char => TRANSLATION.get(char))
  .match(/.{1,5}/g)
  .join(' ')
