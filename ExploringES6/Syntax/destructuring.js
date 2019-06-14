'use strict'

const print = require('../helpers/print')

// exec() returns captured groups via an Array-like object.
const matchObj =
  /^(\d\d)-(\d\d)-(\d\d\d\d)$/
    .exec('06-06-2019')

// In ES5, you need an intermediate variable ( matchObj in the example below),
// even if you are only interested in the groups:
const date = matchObj[0]
const day = matchObj[1]
const month = matchObj[2]
const year = matchObj[3]

print(`
date: ${date}
day: ${day}
month: ${month}
year: ${year}
`)

// In ES6, destructuring makes this code simpler:
const [, d, m, y] = matchObj
print(`
day: ${d}
month: ${m}
year: ${y}
`)

const person = {
  firstName: 'Samuel',
  lastName: 'Thewessen',
  age: 32,
  sex: 'M'
}

const { firstName: first, age, city = 'Amsterdam' } = person
// A new variable age is created and is equal to person.age
print(age)
// A new variable first is created and is equal to person.firstName
print(first)
// person.firstName exists BUT the new variable created is named first
print(firstName)
// A new variable city is created and since person.city is
// undefined, city is equal to the default value provided "Amsterdam".
print(city)
