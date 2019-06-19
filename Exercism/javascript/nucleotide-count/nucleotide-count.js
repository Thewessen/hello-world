'use strict'

const equal = (a) => (b) => a === b

export class NucleotideCounts {
  static parse (dna) {
    const nucleotide = ['A', 'C', 'G', 'T']
    const valid = dna
      .split('')
      .every((e) => nucleotide.includes(e))

    if (!valid) {
      throw new Error('Invalid nucleotide in strand')
    }

    return nucleotide
      .map((e) => equal(e))
      .map((f) => dna.split('').filter((e) => f(e)))
      .map((a) => a.length)
      .join(' ')
  }
}
