const print = require('../helpers/print')

// Arrow function in ES6 allow for a better binding of this.
// Lets look at some ES5 examples first:

// ES5
// =================================
// Wrong example
print('Wrong')
function Prefixer (prefix) {
  this.prefix = prefix
}
Prefixer.prototype.prefixArray = function (arr) { // (A)
  return arr.map(function (x) { // (B)
    return this.prefix + x  // (C)
  })
}
const prefixer = new Prefixer('Hi ')
print(prefixer.prefixArray(['Henk', 'Bart'])) // [ 'undefinedHenk', 'undefinedBart' ]
// In line C, we’d like to access this.prefix,
// but can’t do that because the this of the function from line B
// shadows the this of the method from line A.
// This is undefined in non-method functions,
// which is why we get an error if we use Prefixer in strict mode.

// Binding of this:
// 1. Non-method/constructor functions (undefined)
// 2. Methods ('underlaying' object)
// 3. Constructor (the constructor function??)

// Or in other words:
// - Traditional functions have a dynamic this; its value is determined by how they are called.
// - Arrow functions have a lexical this; its value is determined by the surrounding scope.

print('ES5')
// Fix solution 1
// Create new var for this
Prefixer.prototype.prefixArray = function (arr) {
  var that = this
  return arr.map(function (x) {
    return that.prefix + x
  })
}
print(prefixer.prefixArray(['Henk', 'Bart']))

// Fix solution 2
// Use second map argument (binding for this)
Prefixer.prototype.prefixArray = function (arr) {
  return arr.map(function (x) {
    return this.prefix + x
  }, this)
}
print(prefixer.prefixArray(['Henk', 'Bart']))

// Fix solution 3
// Explicitly bind this
Prefixer.prototype.prefixArray = function (arr) {
  return arr.map(function (x) {
    return this.prefix + x
  }.bind(this))
}
print(prefixer.prefixArray(['Henk', 'Bart']))

// ES6 Arrow function
// =================================
// this is not bind to the arrow function.
print('ES6')
Prefixer.prototype.prefixArray = function (arr) {
  return arr.map((x) => this.prefix + x)
}
print(prefixer.prefixArray(['Henk', 'Bart']))

// Better
class Prefix {
  constructor (prefix) {
    this.prefix = prefix
  }

  prefixArray (arr) {
    return arr.map(function (x) {
      return this.prefix + x
    })
  }
}
const myprefixer = new Prefix('This ')
print(myprefixer.prefixArray(['work', 'job']))
