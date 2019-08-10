'use strict'

export class Crypto {
  constructor (message) {
    this.message = message
  }

  normalizePlaintext() {
    return this.message.replace(/\W/g, '').toLowerCase()
  }

  size() {
    return Math.ceil(Math.sqrt(this.normalizePlaintext().length))
  }

  plaintextSegments() {
    return this.normalizePlaintext()
      .match(new RegExp(`.{1,${this.size()}}`, 'g'))
  }

  ciphertext() {
    return this.plaintextSegments()
      .map((__, i, segments) => segments.map(segment => segment.charAt(i)).join(''))
      .join('')
  }
}
