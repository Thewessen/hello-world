const DNAtoRNA: Map<string, string> = new Map([
  ['G', 'C'],
  ['C', 'G'],
  ['T', 'A'],
  ['A', 'U']
])

class Transcriptor {
  toRna(dna: string): string {
    if (!/^[GCTA]*$/.test(dna)) {
      throw new Error('Invalid input DNA.')
    }
    return dna
      .split('')
      .map((d) => DNAtoRNA.get(d))
      .join('')
  }
}

export default Transcriptor
