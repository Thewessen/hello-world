'use strict'

// const removeTrailingWhitespace = (string) => {
//   const match = string.match(/[\r\n\t\s]+$/)
//   return string.substr(0, match === null ? undefined : match.index)
// }

export const hey = (message = '') => {
  message = message.trim()

  const isUpperCase = /[a-zA-Z]/.test(message) && !/[a-z]/.test(message)
  const isQuestion = /\?$/.test(message)

  if (isUpperCase && isQuestion) return "Calm down, I know what I'm doing!"
  if (isUpperCase) return 'Whoa, chill out!'
  if (isQuestion) return 'Sure.'
  if (message === '') return 'Fine. Be that way!'

  return 'Whatever.'
}
