'use strict'

// Iterate of the entries of an object

module.exports = function * (obj) {
  for (key of Reflect.ownKeys(obj)) {
    yield [key, obj[key]]
  }
}
