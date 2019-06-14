'use strict'

const print = require('../helpers/print')

const twoLoop = (iterable) => {
  for (const x of iterable) {
    print(x)
    break
  }
  for (const x of iterable) {
    print(x)
  }
}
const giveIter = (iterator) => iterator[Symbol.iterator]()

// Some iterators return closable iterables, like generators:
print('closable:')
function * elements () {
  yield 'a'
  yield 'b'
  yield 'c'
}

twoLoop(elements())

// Others, like array's, are not closeable:
print('non-closable:')
const myArr = Array.from('abcd')
twoLoop(giveIter(myArr))

// It is possible to prefent Iters from closing:
class PreventClosing {
  constructor(iterator) {
    this.iterator = iterator
  }
  [Symbol.iterator]() {
    return this
  }
  next () {
    return this.iterator.next()
  }
  return (value = undefined) {
    return { done: false, value }
  }
}
print('prevent closing:')
twoLoop(new PreventClosing(elements()))

// Other method:
print('prevent closing:')
elements.prototype.return = undefined
twoLoop(elements())
