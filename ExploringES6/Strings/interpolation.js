'use strict'

const print = require('../helpers/print')

// In ES6 you can use string interpolation via template literals:
const printCoords = (x, y) => {
  print(`(${x},${y})`)
}
printCoords(3, 5)
