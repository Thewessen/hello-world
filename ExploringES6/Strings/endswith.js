'use strict'

const { methodCallToString: str } = require('../helpers/helpers')
const print = require('../helpers/print')

// The ECMAScript 6 standard library provides several new methods for strings.
// index >= 0 && index === str.length-suffix.length is the same as:
const fullName = 'Samuel Thewessen'
print(str(fullName, ''.endsWith, 'el'))
print(str(fullName, ''.endsWith, 'en'))
