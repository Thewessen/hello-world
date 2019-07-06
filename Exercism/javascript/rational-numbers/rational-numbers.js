'use strict'

const gcd = (a, b) => b ? gcd(b, a % b) : a

export class Rational {
  constructor (a, b) {
    this.p = a
    this.q = b
  }

  norm (fraq1, fraq2) {
    const div = fraq1.q * fraq2.q
    return [
      new Rational(fraq1.p * fraq2.q, div),
      new Rational(fraq2.p * fraq1.q, div)
    ]
  }

  add (fraq) {
    const [ f1, f2 ] = this.norm(this, fraq)
    return new Rational(f1.p + f2.p, f2.q).reduce()
  }

  sub (fraq) {
    const [ f1, f2 ] = this.norm(this, fraq)
    return new Rational(f1.p - f2.p, f2.q).reduce()
  }

  mul (fraq) {
    const {p, q} = this
    return new Rational(p * fraq.p, q * fraq.q).reduce()
  }

  div (fraq) {
    const {p, q} = this
    return new Rational(p * fraq.q, q * fraq.p).reduce()
  }

  abs () {
    return new Rational(Math.abs(this.p), this.q).reduce()
  }

  exprational (int) {
    return new Rational(this.p ** int, this.q ** int).reduce()
  }

  expreal (int) {
    const {p, q} = this.reduce()
    return 10 ** (Math.log10(int ** p) / q)
  }

  reduce () {
    const { abs, sign } = Math
    const {p, q} = this
    if (q === 0) {
      throw new Error('Denominator can not be zero!')
    }
    if (p === 0) {
      return new Rational(0, 1)
    } else {
      const fraq = [p, q].map(abs)
      const d = gcd(...fraq)
      return new Rational(
        ...fraq
        .map((x) => x / d)
        .map((x, i) => !i ? sign(p) * sign(q) * x : x)
      )
    }
  }
}
