class Bob {
  hey (text: string): string {
    const message = text.trim()

    const isUpperCase = /[a-zA-Z]/.test(message) && !/[a-z]/.test(message)
    const isQuestion = message.endsWith('?')

    if (isUpperCase && isQuestion) {
      return "Calm down, I know what I'm doing!"
    }
    if (isUpperCase) {
      return 'Whoa, chill out!'
    }
    if (isQuestion) {
      return 'Sure.'
    }
    if (message === '') {
      return 'Fine. Be that way!'
    }
    return 'Whatever.'
  }
}

export default Bob
