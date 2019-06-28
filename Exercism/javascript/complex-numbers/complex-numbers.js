'use strict'

const squared = (i) => i ** 2
const sum = (a, b) => a + b

export class ComplexNumber {
  constructor (real = 0, imag = 0) {
    this._real = real
    this._imag = imag
  }

  get real () {
    return this._real
  }

  get imag () {
    return this._imag
  }

  get abs () {
    return Math.hypot(this.real, this.imag)
  }

  get conj () {
    const [a, b] = [...Object.values(this)]
    return new ComplexNumber(
      a,
      0 - b
    )
  }

  get exp () {
    const [a, b] = [...Object.values(this)]
    const { E, cos, sin } = Math
    return new ComplexNumber(
      E ** a * cos(b),
      E ** a * sin(b)
    )
  }

  add (complex) {
    const [a, b, c, d] =
      [...Object.values(this), ...Object.values(complex)]
    return new ComplexNumber(
      sum(a, c),
      sum(b, d)
    )
  }

  sub (complex) {
    const [a, b, c, d] =
      [...Object.values(this), ...Object.values(complex)]
    return new ComplexNumber(
      a - c,
      b - d
    )
  }

  div (complex) {
    const [a, b, c, d] =
      [...Object.values(this), ...Object.values(complex)]
    const divide = [c, d].map(squared).reduce(sum)
    return new ComplexNumber(
      (a * c + b * d) / divide,
      (b * c - a * d) / divide
    )
  }

  mul (complex) {
    const [a, b, c, d] =
      [...Object.values(this), ...Object.values(complex)]
    return new ComplexNumber(
      a * c - b * d,
      b * c + a * d
    )
  }

  toString () {
    const [a, b] = [...Object.values(this)]
    const { abs } = Math
    return `${a}${b < 0 ? ` - ${abs(b)}` : ` + ${b}`}i`
  }
}
