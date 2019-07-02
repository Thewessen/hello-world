'use strict'

const zip = (...arrays) => {
  let iters = arrays.map((array) => array[Symbol.iterator]())
  let items = iters.map((iter) => iter.next())
  let columns = []
  while (!items.some((item) => item.done)) {
    columns.push(items.map((item) => item.value))
    items = iters.map((iter) => iter.next())
  }
  return columns
}

export class Matrix {
  constructor (string) {
    this._rows = string
      .split('\n')
      .map((row) => row
        .trim()
        .split(' ')
        .map(Number)
      )
    this._columns = zip(...this.rows)
  }

  get rows() {
    return this._rows
  }

  get columns() {
    return this._columns
  }

  * _saddlePoints () {
    const { _rows, _columns } = this
    for (const i in _rows) {
      for (const j in _rows[i]) {
        if (
          _rows[i].every((n) => n <= _rows[i][j]) &&
          _columns[j].every((n) => n >= _rows[i][j])
        ) { yield [i, j].map(Number) }
      }
    }
  }

  get saddlePoints() {
    return [...this._saddlePoints()]
  }
}
