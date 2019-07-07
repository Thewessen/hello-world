'use strict'

class Result {
  constructor(start, end) {
    this.start = start
    this.end = end
  }
}

const reverseStr = (str) => str.split('').reverse().join('')
const identity = (value) => value
const shiftOne = (arr) => arr.map((str, i) => str.substr(i))
const reverse = (arr) => [...arr].reverse()
const reverseLines = (arr) => arr.map(reverseStr)
const order = (f, g) => (...args) => f(g(...args))
const combine = (...fns) => (...args) => fns.reduce(order)(...args)

const search = (dir, adjust) => (word, lines) => {
  for (const [index, line] of dir(lines).entries()) {
    if (line.includes(word)) {
      const str = line.search(word)
      const len = word.length
      return new Result(
        adjust([[index + 1, str + 1], line])[0],
        adjust([[index + 1, str + len], line])[0]
      )
    }
  }
}

const resultRev = ([[x, y], line]) =>
  [[x, line.length - y + 1], line]
const resultVert = ([[x, y], line]) =>
  [[y, x], line]
const resultShift = ([[x, y], line]) =>
  [[x, y + x - 1], ' '.repeat(x - 1) + line]
const resultRevShift = ([[x, y] , line]) =>
  [[x, line.length - x + 1], line]

// const resultRevShift = combine(resultShift, resultRev, resultVert)

const resultVertRev = combine(resultVert, resultRev)

const horizontal = identity

const horizontalRev = reverseLines

const vertical = (grid) => grid
  .reduce((acc, line) => {
    line.split('').forEach((char, i) => {
      acc[i] = acc[i] ? acc[i] + char : char
    })
    return acc
  }, [])

const verticalRev = combine(vertical, reverse)

const diagonalTopRight = combine(vertical, shiftOne)
const resultTR = combine(resultShift, resultVert)
const diagonalTopLeft = combine(diagonalTopRight, reverseLines)
const resultTL = combine(resultRevShift, resultVert)
const diagonalLeftTop = combine(reverseLines, diagonalTopLeft)
const resultLT = combine(resultTL, resultRev)
const diagonalLeftBottom = combine(diagonalTopRight, vertical)
const resultLB = combine(resultVert, resultTR)
const diagonalRightTop = combine(reverseLines, diagonalTopRight)
const resultRT = combine(resultTR, resultRev)
const diagonalRightBottom = combine(diagonalRightTop, reverse)
const resultRB = combine(resultVert, resultRevShift, resultVert)
const diagonalBottomRight = combine(diagonalTopRight, reverse)
const resultBR = combine(resultRB, resultRev)
const diagonalBottomLeft = combine(reverseLines, diagonalLeftBottom)
const resultBL = combine(resultLB, resultRev)

// const diagonal = (grid) =>
//   vertical(vertical(grid).map(shiftOne))
//   .slice(1).concat(vertical(grid.map(shiftOne)))

// const diagonalRev = (grid) =>
//   diagonal(horizontalRev(grid))

const grid = [
  'jefblpepre',
  'camdcimgtc',
  'oivokprjsm',
  'pbwasqroua',
  'rixilelhrs',
  'wolcqlirpc',
  'screeaumgr',
  'alxhpburyi',
  'jalaycalmp',
  'clojurermt',
]
module.exports = search(diagonalRightBottom, resultRB)('bmip', grid)
// module.exports = diagonalRightBottom(grid)

// export default class WordSearch {
class WordSearch {
  constructor (grid) {
    this.grid = grid
  }

  find (words) {
    let result = {}
    let searches = [
      search(horizontal, identity),
      search(vertical, resultVert),
      // search(diagonal, identity),
      search(horizontalRev, resultRev),
      search(verticalRev, resultVertRev)
      // search(diagonalRev, identity)
    ]
    for (const word of words) {
      for (const srch of searches) {
        result[word] = srch(word, this.grid)
        if (result[word]) {
          break
        }
      }
    }
    return result
  }
}
