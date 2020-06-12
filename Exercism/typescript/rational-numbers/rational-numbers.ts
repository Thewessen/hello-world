export default class Rational {
  constructor(
    private p: number,
    private q: number,
    private san: boolean = true
  ) {
    if (!q || isNaN(q)) {
      throw new Error(`Invalid denominator: ${q}`)
    }
    if (san) this.reduce().sanitize()
  }

  add(n: Rational): Rational {
    const [{p: a}, {p, q}] = this.norm(n)
    return new Rational(a + p, q)
  }

  sub(n: Rational): Rational {
    const [{p: a}, {p, q}] = this.norm(n)
    return new Rational(a - p, q)
  }

  mul({p, q}: Rational): Rational {
    const {p: a, q: b} = this
    return new Rational(a * p, b * q)
  }

  div({p, q}: Rational): Rational {
    const {p: a, q: b} = this
    return new Rational(a * q, b * p)
  }

  abs(): Rational {
    const {p, q} = this
    return new Rational(Math.abs(p), Math.abs(q))
  }

  exprational(n: number): Rational {
    const {p, q} = this
    return new Rational(p ** n, q ** n)
  }

  expreal(n: number): number {
    const {p: a, q: b} = this
    return Rational.prime_factorization(n)
      .map(([p, n]) => [p, n * a / b])
      .reduce((acc, [p, n]) => acc * p ** n, 1)
  }

  reduce(): Rational {
    const {abs} = Math
    const g = Rational.gcd(abs(this.p), abs(this.q))
    this.p /= g
    this.q /= g
    return this
  }

  private norm ({p, q}: Rational): Rational[] {
    const {p: a, q: b} = this
    return [
      new Rational(a * q, b * q, false),
      new Rational(b * p, b * q, false)
    ]
  }

  private sanitize(): void {
    const {p, q} = this
    const {sign, abs} = Math

    // converts -0 and +0 to 0
    let nom = (p === 0 ? 0 : p)
    // neg denom should inverse sign on nom
    nom *= sign(q)

    this.p = nom
    this.q = abs(q)
  }

  private static prime_factorization(n: number): number[][] {
    let p = 2
    let count = 0
    const factors = []
    while (p <= n) {
      while (n % p === 0) {
        n /= p
        count += 1
      }
      if (count > 0) factors.push([p, count])
      p += 1
      count = 0
    }
    return factors
  }

  private static gcd (a: number, b: number): number {
    return b ? Rational.gcd(b, a % b) : a
  }
}
