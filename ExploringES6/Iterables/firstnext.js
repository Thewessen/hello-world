'use strict'

const print = require('../helpers/print')
const coroutine = require('../helpers/coroutine')

// When using a generator as an observer, it is important to note that the only purpose of the first
// invocation of next() is to start the observer. It is only ready for input afterwards, because this
// first invocation advances execution to the first yield . Therefore, any input you send via the first
// next() is ignored:

const genFunc = function * () {
  print(`First input: ${yield}`)
  return print('DONE')
}

let myIter = genFunc()
myIter.next('a')
myIter.next('b')

// The helperfunction coroutine (see docs) helps by calling the first .next()
// for us.

const wrapped = coroutine(genFunc)
const iter = wrapped()
iter.next('a')
iter.next('b')
