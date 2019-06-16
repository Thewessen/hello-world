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
  constructor(stringMatrix) {
    this._rows = stringMatrix
      .split('\n')
      .map((row) => row.split(' ').map((i) => Number.parseInt(i)))
    this._columns = zip(...this.rows)
  }
  
  get rows () {
    return this._rows
  }

  get columns () {
    return this._columns
  }
}
