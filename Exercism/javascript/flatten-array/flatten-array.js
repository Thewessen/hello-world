'use strict'

// for some reasons the tests uses a class
export class Flattener {
  flatten (arr) {
    if (!Array.isArray(arr)) {
      throw new Error('Argument is not an array')
    }
    return arr
      .reduce((acc, curr) => {
        if (Array.isArray(curr)) {
          acc.push(...this.flatten(curr))
        } else {
          acc.push(curr)
        }
        return acc
      }, [])
      .filter((el) => el !== null)
      .filter((el) => typeof el !== 'undefined')
  }
}
