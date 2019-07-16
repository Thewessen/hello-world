'use strict'

export class Board {
  constructor (board) {
    this.board = board
      .map((row) => row.trim().split(' '))
  }

  static go (position, dir) {
    return position.map((xy, i) => xy + dir[i])
  }

  static directions() {
    return [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0],
      [1, -1],
      [-1, 1]
    ]
  }

  static pathFinder (board, symbol, finished) {
    return function finder ([x, y]) {
      if (x === finished[0] || y === finished[1]) {
        return true
      }
      board.clear([x, y])
      for (const dir of Board.directions()) {
        const newPos = Board.go([x, y], dir)
        if(
          board.at(newPos) === symbol &&
          finder(newPos, symbol, finished)
        ) {
          return true
        }
      }
      return false
    }
  }

  at ([x, y]) {
    if (this.board[x]) {
      return this.board[x][y]
    }
  }

  clear ([x, y]) {
    this.board[x][y] = '.'
  }

  winner() {
    if (this.board
      .map((__, i) => [i, 0])
      .filter((p) => this.at(p) === 'X')
      .some(Board.pathFinder(
          this, 'X',
          [null, this.board[0].length - 1]
        ))
    ) { return 'X' }
    if (this.board
      .map((__, i) => [0, i])
      .filter((p) => this.at(p) === 'O')
      .some(Board.pathFinder(
        this, 'O',
        [this.board.length - 1, null]))
    ) { return 'O' }
    return ''
  }
}
