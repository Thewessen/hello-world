'use strict'

const print = require('../helpers/print')

let localVar = 'this var is only local too the module!'

const myFunc = (mess) => {
  print(`${mess}, ${localVar}`)
}
module.exports = myFunc
