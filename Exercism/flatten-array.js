'use strict'

// Take a nested list and return a single flattened list with all values except nil/null.

// The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

// For Example
// input: [1,[2,3,null,4],[null],5]
// output: [1,2,3,4,5]

// for some reasons the test wants a class
class Flattener {
  flatten (arr) {
    if (!Array.isArray(arr)) {
      throw new Error('Argument is not an array')
    }
    return arr
      .reduce((acc, curr) => {
        if (Array.isArray(curr)) {
          acc = acc.concat(this.flatten(curr))
        } else {
          acc.push(curr)
        }
        return acc
      }, [])
      .filter((el) => el !== null)
      .filter((el) => typeof el !== 'undefined')
  }
}

module.exports = Flattener
