'use strict'

const print = require('../helpers/print')
const { methodCallToString: str } = require('../helpers/helpers')

// ES6 comes with a new .findIndex method for Arrays.
// (instead of indexOf method)
// This gives the oppertunity for search by function:

const myarr = [1, 3, 'abc', undefined, NaN]

print(str(myarr, [].findIndex, (x) => typeof x === 'undefined'))
print(str(myarr, [].findIndex, (x) => typeof x === 'string'))
print(str(myarr, [].findIndex, (x) => Number.isNaN(x)))
