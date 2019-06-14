'use strict'

// A helperfunction that invoces the first next() for us.
module.exports = function (genFunc) {
  return function (...args) {
    const genObj = genFunc(...args)
    genObj.next()
    return genObj
  }
}
