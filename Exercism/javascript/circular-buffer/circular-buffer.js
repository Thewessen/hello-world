'use strict'


class BufferEmptyError extends Error {
  constructor () {
    super('Buffer empty')
  }
}

class BufferFullError extends Error {
  constructor () {
    super('Buffer full!')
  }
}

class CircularBuffer {
  constructor (int) {
    this.buffer = Array(int).fill(null)
    this.r = 0
    this.w = 0
  }

  get size () {
    return this.buffer.length
  }

  read () {
    const { buffer, r, size } = this
    if (buffer[r] === null) {
      throw new BufferEmptyError()
    }
    const value = buffer[r]
    buffer[r] = null
    this.r = inc(r, size)
    return value
  }

  write (value) {
    if (!isValue(value)) {
      return
    }
    const { buffer, w, size } = this
    if (buffer[w] !== null) {
      throw new BufferFullError()
    }
    buffer[w] = value
    this.w = inc(w, size)
  }

  forceWrite (value) {
    if (!isValue(value)) {
      return
    }
    const { buffer, w, r, size } = this
    buffer[w] = value
    if (r === w) {
      this.r = inc(r, size)
    }
    this.w = inc(w, size)
  }
  
  clear () {
    this.buffer = this.buffer.map(() => null)
  }
}

const inc = (nr, mod) => (nr + 1) % mod
const isValue = (value) =>
  typeof value !== 'undefined' && value !== null

const circularBuffer = (int) => new CircularBuffer(int)

export {
  BufferFullError,
  BufferEmptyError
}

export default circularBuffer
