'use strict'

const equal_coord = ([x1, y1], [x2, y2]) => x1 === x2 && y1 === y2

export class QueenAttack {
  constructor (position = { white: [0, 3], black: [7, 3]}) {
    if (equal_coord(position.white, position.black)) {
      throw new Error('Queens cannot share the same space')
    }
    Object.assign(this, position)
  }

  toString () {
    const [x1, y1] = this.white
    const [x2, y2] = this.black
    const emptyBoard = Array.from({ length: 8 }, () => Array(8).fill('_'))
    emptyBoard[x1][y1] = 'W'
    emptyBoard[x2][y2] = 'B'
    return emptyBoard.map(row => row.join(' ')).join('\n') + '\n'
  }

  canAttack () {
    const [x1, y1] = this.white
    const [x2, y2] = this.black
    return x1 === x2
      || y1 === y2
      || y1 - x1 === y2 - x2
      || y1 + x1 === y2 + x2
  }
}
