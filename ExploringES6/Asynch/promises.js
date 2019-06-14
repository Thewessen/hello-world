'use strict'

const print = require('../helpers/print')

// A short tryout

async function brave () {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('brave')
    }, 200)
  })
}

function newer () {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('new')
    }, 400)
  })
}
function world () {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('world')
    }, 600)
  })
}

async function logAfter1200 () {
  const first = await brave()
  const second = await newer()
  const last = await world()
  print(`logAfter1200: ${first} ${second} ${last}`)
}
logAfter1200()

async function logAfter600 () {
  const [first, second, last] = await Promise.all([brave(), newer(), world()])
  print(`logAfter600: ${first} ${second} ${last}`)
}
logAfter600()
