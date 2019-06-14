'use strict'

const { methodCallToString: str } = require('../helpers/helpers')
const print = require('../helpers/print')

// The ECMAScript 6 standard library provides several new methods for strings.
// str.indexOf('x') === 0 is the same as:
const fullName = 'Samuel Thewessen'
print(str(fullName, ''.startsWith, 'Sa'))
print(str(fullName, ''.startsWith, 'Th'))
