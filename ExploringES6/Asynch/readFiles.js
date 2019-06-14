'use strict'

const fs = require('fs')
const print = require('../helpers/print')
const warn = require('../helpers/warn')

// Reading files an using datastream using node_module fs
// This function is using a callback
fs.readFile('./file.txt', { encoding: 'utf8' }, (error, text) => {
  if (error) {
    warn(error)
  }
  print(text)
})

const readFilePromise = (filename) =>
  new Promise((resolve, reject) =>
    fs.readFile(filename, { encoding: 'utf8' }, (error, data) => {
      if(error) { 
        reject(error)
      } else {
        resolve(data)
      }
    })
  )

// With a promisified version, you can use readFile like this:
readFilePromise('./file.txt')
  .then((text) => print(`Promise: ${text}`))
  .catch((error) => warn(error))

