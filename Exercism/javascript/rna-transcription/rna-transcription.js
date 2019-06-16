'use strict'

const DNAtoRNA = new Map([
  ['G', 'C'],
  ['C', 'G'],
  ['T', 'A'],
  ['A', 'U']
])

export const toRna = (dna) => dna
  .split('')
  .map((d) => DNAtoRNA.get(d))
  .join('')
