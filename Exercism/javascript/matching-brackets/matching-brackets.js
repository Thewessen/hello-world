'use strict'

const PAIRS = /\(\)|\[\]|\{\}/

export const matchingBrackets = (brackets) => {
  if (brackets === '') {
    return true
  }
  if (PAIRS.test(brackets)) {
    return matchingBrackets(
      brackets.replace(PAIRS, '')
    )
  }
  return false
}
