'use strict'

const RHYMES = [
  ['fly', "I don't know why she swallowed the fly. Perhaps she'll die."],
  ['spider', 'It wriggled and jiggled and tickled inside her.'],
  ['bird', 'How absurd to swallow a bird!'],
  ['cat', 'Imagine that, to swallow a cat!'],
  ['dog', 'What a hog, to swallow a dog!'],
  ['goat', 'Just opened her throat and swallowed a goat!'],
  ['cow', "I don't know how she swallowed a cow!"],
  ['horse', "She's dead, of course!"]
]

const first = (anim, sntc) =>
`I know an old lady who swallowed a ${anim}.
${sntc}
`

const last = (anim1, anim2) =>
`She swallowed the ${anim1} to catch the ${anim2}.
`

export class Song {
  verse (nr) {
    let i = nr - 1
    let vers = ''
    while (i >= 0) {
      let [anim, sntc] = RHYMES[i]
      if (nr === 8) {
        vers = first(anim, sntc)
        break
      }
      if (i === 1 && nr !== 2) {
        anim += ` that ${sntc.split(' ').slice(1).join(' ').replace('.','')}`
      }
      if (i === nr - 1) {
        vers += first(anim, sntc)
        i -= 1
        continue
      }
      vers += last(RHYMES[i + 1][0], anim)
      if (i === 0 && nr !== 1) {
        vers += `${sntc}\n`
      }
      i -= 1
    }
    return vers
  }

  verses (from, to) {
    let vers = ''
    for (let i = from; i <= to; i += 1) {
      vers += this.verse(i)
      vers += '\n'
    }
    return vers
  }
}
