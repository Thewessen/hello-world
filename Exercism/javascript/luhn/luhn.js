'use strict'

const even = (nr) => nr % 2 === 0

export class Luhn {
  constructor (string) {
    this.creditnr = string
  }

  get valid () {
    const chars = [...this.creditnr.replace(/ /g, '')]
      .reverse()
      .map(Number)
    return chars.length > 1 &&
      !chars
        .some(isNaN) &&
      chars
        .filter((__, idx) => !even(idx))
        .map((nr) => nr * 2)
        .map((nr) => nr > 9 ? nr - 9 : nr)
        .concat(chars.filter((__, idx) => even(idx)))
        .reduce((a, b) => a + b) % 10 === 0
  }
}
