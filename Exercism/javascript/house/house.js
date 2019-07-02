'use strict'

const VERSE = [
  ['', 'horse and the hound and the horn'],
  ['belonged to', 'farmer sowing his corn'],
  ['kept', 'rooster that crowed in the morn'],
  ['woke', 'priest all shaven and shorn'],
  ['married', 'man all tattered and torn'],
  ['kissed', 'maiden all forlorn'],
  ['milked', 'cow with the crumpled horn'],
  ['tossed', 'dog'],
  ['worried', 'cat'],
  ['killed', 'rat'],
  ['ate', 'malt'],
  ['lay in', 'house that Jack built.']
]
export class House {
  static verse (nr) {
    let i = VERSE.length - nr 
    let lyrics = []
    while (i < VERSE.length) {
      const [a, b] = VERSE[i]
      if (i === VERSE.length - nr) {
        lyrics.push(`This is the ${b}`)
      } else {
        lyrics.push(`that ${a} the ${b}`)
      }
      i += 1
    }
    return lyrics
  }

  static verses(from, to) {
    let lyrics = []
    for (let i = from; i <= to; i += 1) {
      lyrics = lyrics.concat(this.verse(i))
      lyrics.push('')
    }
    return lyrics.slice(0, lyrics.length - 1)
  }
}
