'use strict'

export class Flattener {
  flatten (arr) {
    const { isArray } = Array
    if (!isArray(arr)) {
      throw new Error('Argument is not an array')
    }
    return arr
      .reduce((acc, curr) =>
        isArray(curr)
          ? [...acc, ...this.flatten(curr)]
          : [...acc, curr]
      , [])
      .filter((el) => el !== null)
      .filter((el) => typeof el !== 'undefined')
  }
}
