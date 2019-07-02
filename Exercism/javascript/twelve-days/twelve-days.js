'use strict'

const NUMBER = new Map([
  { word: 'zero', th: 'zeroth' },
  { word: 'and', th: 'first' },
  { word: 'two', th: 'second' },
  { word: 'three', th: 'third' },
  { word: 'four', th: 'fourth' },
  { word: 'five', th: 'fifth' },
  { word: 'six', th: 'sixth' },
  { word: 'seven', th: 'seventh' },
  { word: 'eight', th: 'eighth' },
  { word: 'nine', th: 'ninth' },
  { word: 'ten', th: 'tenth' },
  { word: 'eleven', th: 'eleventh' },
  { word: 'twelve', th: 'twelfth' },
].entries())

const PRESENTS = [
  'Drummers Drumming',
  'Pipers Piping',
  'Lords-a-Leaping',
  'Ladies Dancing',
  'Maids-a-Milking',
  'Swans-a-Swimming',
  'Geese-a-Laying',
  'Gold Rings',
  'Calling Birds',
  'French Hens',
  'Turtle Doves',
  'a Partridge in a Pear Tree.'
]

export const recite = (from, to = undefined) => {
  let verse = ''
  to = to || from
  for (let i = from; i <= to; i += 1) {
    const presents = PRESENTS
      .slice(PRESENTS.length - i)
      .map((p, idx, arr) => `${
        arr.length > 1
          ? ' ' + NUMBER.get(arr.length - idx).word
          : ''
        } ${p}`)
      .join(',')
    verse += `On the ${NUMBER.get(i).th} day of Christmas my true love gave to me:${presents}\n\n`
  }
  return verse.replace(/\n$/, '')
}
