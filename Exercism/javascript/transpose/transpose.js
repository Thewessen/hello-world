'use strict'

const ljust = (size, string) => {
  return ' '.repeat(size - string.length) + string
}

export const transpose = (lines) =>
  lines
    .reduce((trans, line, idx) => {
      line.split``.forEach(
        (char, i) => {
          const s = trans[i] || ''
          trans[i] = s + ljust(idx - s.length + 1, char)
        }
      )
      return trans
    }, [])
