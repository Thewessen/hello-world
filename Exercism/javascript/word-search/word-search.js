'use strict'

const add = (point, delta) =>
  point.map((n, i) => n + delta[i])

class Result {
  constructor(start, end) {
    this.start = start
    this.end = end
  }
}

class Grid {
  constructor (grid) {
    this.grid = grid
  }

  * traverse (start, delta) {
    let [i, j] = start
    while (i >= 0 && j >= 0 && this.grid[i] && this.grid[i][j]) {
      yield this.grid[i][j];
      [i, j] = add([i, j], delta)
    }
  }

  * allPoints () {
    for (const i in this.grid) {
      for (const j in this.grid[i]) {
        yield [i, j].map(Number)
      }
    }
  }
}

export default class WordSearch extends Grid {
  constructor (grid) {
    super(grid)
    this.deltas = [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0],
      [1, 1],
      [1, -1],
      [-1, -1],
      [-1, 1]
    ]
  }

  find (words) {
    const result = {}
    words: for (const word of words) {
      result[word] = undefined
      points: for (const start of this.allPoints()) {
        for (const delta of this.deltas) {
          let w = ''
          for (const char of this.traverse(start, delta)) {
            w += char
            if (!word.startsWith(w)) {
              if (w.length === 1) {
                continue points
              }
              break
            }
            if (w === word) {
              const end = start.map(
                (n, i) => n + delta[i] * (w.length - 1)
              )
              result[word] = new Result(
                ...[start, end].map((a) => a.map((n) => n + 1))
              )
              continue words
            }
          }
        }
      }
    }
    return result
  }
}
