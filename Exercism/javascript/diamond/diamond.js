'use strict'

const mirror = (array) =>
  array.concat([...array].reverse().slice(1))

export class Diamond {
  makeDiamond (char) {
    const start = 'A'.charCodeAt()
    const diff = char.charCodeAt() - start
    return mirror(Array.from(
      { length: diff + 1 },
      (__, i) => Array.from(
        { length: diff + 1 },
        (__, j) =>
          i === diff - j
            ? String.fromCharCode(start + i)
            : ' '
      )
    ).map(mirror))
    .map((line) => line.join(''))
    .join('\n') + '\n'
  }
}
