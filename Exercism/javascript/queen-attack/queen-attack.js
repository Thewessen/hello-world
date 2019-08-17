'use strict'

const equalCoord = ([x1, y1], [x2, y2]) => x1 === x2 && y1 === y2
const sameRow = ([, a], [, b]) => a === b
const sameColumn = ([a,], [b,]) => a === b
const sameDiagonal = ([x1, y1], [x2, y2]) =>
    y1 - x1 === y2 - x2 || y1 + x1 === y2 + x2

class ChessBoard {
  constructor () {
    this.board = Array.from(
      { length: 8 }, () => Array(8).fill('_')
    )
  }

  toString () {
    return this.board
      .map(row => row.join(' '))
      .join('\n') + '\n'
  }

  setPiece (piece, [x, y]) {
    this.board[x][y] = piece
  }
}

export class QueenAttack extends ChessBoard {
  constructor (position) {
    const { white, black } = position || { white: [0, 3], black: [7, 3] }
    if (equalCoord(white, black)) {
      throw new Error('Queens cannot share the same space')
    }
    super()
    this.setPiece('W', white)
    this.setPiece('B', black)
    this.white = white
    this.black = black
  }

  canAttack () {
    const { white, black } = this
    return sameRow(white, black)
      || sameColumn(white, black)
      || sameDiagonal(white, black)
  }
}
