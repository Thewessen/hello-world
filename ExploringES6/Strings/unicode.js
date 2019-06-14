'use strict'

const print = require('../helpers/print')

// ES6 alows unicode characters in strings:
const unicode = 'a\uD83D\uDC0A'
print(unicode)

// On iteration, \uD83D\uDC0A is one character, as it should be:
for (let char of unicode) {
  print(char)
}
