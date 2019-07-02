'use strict'

export class ISBN {
  constructor (code) {
    this.isbn = code.replace(/-/g, '')
  }

  isValid () {
    return /^[0-9]{9}[0-9X]$/.test(this.isbn) &&
      this.isbn
        .split('')
        .map((nr) => nr === 'X' ? 10 : Number(nr))
        .map((nr, i) => nr * (10 - i))
        .reduce((a, b) => a + b) % 11 === 0
  }
}
