'use strict'

// Object.entriesFrom (ES9) would be nice!
export const transform = (obj) =>
  Object.assign({},
    ...Object.entries(obj)
      .reduce((acc, curr) =>
        [...acc, ...curr[1].map((letter) =>
          ({ [letter.toLowerCase()]: Number.parseInt(curr[0]) })
        )]
      , []))
