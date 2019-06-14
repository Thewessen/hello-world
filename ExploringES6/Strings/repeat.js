'use strict'

const { methodCallToString: str } = require('../helpers/helpers')
const print = require('../helpers/print')

// The ECMAScript 6 standard library provides several new methods for strings.
// The ES5 syntax is more of a hack, new Array(3+1).join('-'):
const string = '-'
print(str(string, ''.repeat, 0))
print(str(string, ''.repeat, 3))
