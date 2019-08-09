'use strict'

export class RotationalCipher {
  static rotate(string, key) {
    return string
      .replace(/[a-z]/ig, char => {
          const base = /[A-Z]/.test(char) 
            ? 'A'.charCodeAt()
            : 'a'.charCodeAt()
          return String.fromCharCode(
            (char.charCodeAt() - base + key) % 26 + base
          )
      })
  }
}
