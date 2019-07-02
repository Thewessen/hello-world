'use strict'

const beer = (i) => `${i || 'no more'} bottle${i !== 1 ? 's' : ''} of beer`
const wall = (i) => `${beer(i)} on the wall`

export class BeerSong {
  static verse (i) {
    return `${wall(i).toUpperCase()[0] + wall(i).slice(1)}, ${beer(i)}.\n` +
      (i === 0
        ? `Go to the store and buy some more, ${wall(99)}.\n`
        : `Take ${i !== 1 ? 'one' : 'it'} down and pass it around, ${wall(i - 1)}.\n`)
  }

  static sing (from = 99, to = 0) {
    return this.verse(from) +
      (from === to ? '' : '\n' + this.sing(from - 1, to))
  }
}
