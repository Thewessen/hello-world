const SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
const FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
const INTERVALS = new Map([['m', 1], ['M', 2], ['A', 3]])
const TONE = /^[a-gA-G][#b]?$/
const useSharps = new Set([
  'C', 'G', 'D', 'A', 'E', 'B', 'F#',
  'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#'
])

export class Scale {
  constructor(tonic) {
    this.tonic = tonic || 'C'
  }

  get tone() {
    return this.tonic[0].toUpperCase() + this.tonic.slice(1)
  }

  chromatic() {
    const chrd = useSharps.has(this.tonic)
      ? SHARPS
      : FLATS
    const i = chrd.indexOf(this.tone)
    return [...chrd.slice(i), ...chrd.slice(0, i)]
  }

  interval(intervals) {
    const chrd = this.chromatic()
    return [...intervals]
      .map(interval => INTERVALS.get(interval))
      .reduce((acc, i) =>
        [...acc, acc[acc.length - 1] + i], [0])
      .map(i => chrd[i])
      .filter(tone => TONE.test(tone))
  }
}
