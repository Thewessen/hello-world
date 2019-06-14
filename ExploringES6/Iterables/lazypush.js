'use strict'

const print = require('./print')
const coroutine = require('../helpers/coroutine')

// Pushes the items of iterable into a generator 'sink'
function send (iterable, sink) {
  for (const x of iterable) {
    sink.next(x)
  }
  // Close the generator when we are done
  sink.return()
}

// Logs the items pushed to it.
// coroutine invoces the first .next() for us.
const logItems = coroutine(function * () {
  try {
    while (true) {
      const item = yield
      print(item)
    }
  }
  finally {
    print('DONE!')
  }
})

send('abcdef', logItems())
