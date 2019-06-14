'use strict'

// Check if an object is a function
module.exports = (obj) => {
  return {}.toString.call(obj) === '[object Function]'
}
