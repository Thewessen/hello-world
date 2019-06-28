'use strict'

const PAIRS = new Map([
  ['[', ']'],
  ['{', '}'],
  ['(', ')']
])

const isOpen = (char) => PAIRS.has(char)
const isClose = (char) => [...PAIRS.values()].includes(char)

const matchingBrackets = (brackets) => {
  if (brackets === '') {
    return true
  }
  if (isOpen(brackets[0])) {
    const match = matchingBrackets(brackets.substr(1))
    if (PAIRS.get(brackets[0]) === match[0]) {
      if (match.length > 1) {
        return matchingBrackets(match.substr(1))
      }
      return true
    }
    return  false
  }
  if (isClose(brackets[0]) && matchingBrackets(brackets.substr(1))) {
    return brackets
  }
  return false
}

module.exports = matchingBrackets
