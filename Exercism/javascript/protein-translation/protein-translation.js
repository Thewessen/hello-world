'use strict'

const CODON = new Map([
  ['AUG',	'Methionine'],
  ...['UUU', 'UUC'].map((e) => [e,	'Phenylalanine']),
  ...['UUA', 'UUG'].map((e) => [e,	'Leucine']),
  ...['UCU', 'UCC', 'UCA', 'UCG'].map((e) =>	[e, 'Serine']),
  ...['UAU', 'UAC'].map((e) => [e,	'Tyrosine']),
  ...['UGU', 'UGC'].map((e) => [e,	'Cysteine']),
  ['UGG',	'Tryptophan'],
  ...['UAA', 'UAG', 'UGA'].map((e) => [e,	'STOP'])
])

export const translate = (rna) => {
  if (!rna) {
    return []
  }
  const result = []
  for (const codon of rna.match(/.{3}/g)) {
    if (CODON.get(codon) === 'STOP') {
      break
    }
    if (!CODON.has(codon)) {
      throw new Error('Invalid codon')
    }
    result.push(CODON.get(codon))
  }
  return result
}
