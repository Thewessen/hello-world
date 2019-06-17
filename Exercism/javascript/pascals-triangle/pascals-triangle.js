'use strict'

export class Triangle {
  constructor (index) {
    if (!Number.isInteger(index)) {
      throw new Error('Constructor argument is not an integer')
    }
    let row = []
    const nextRow = (e, i, arr) => e + (arr[i - 1] || 0)
    this._rows = Array.from({
      [Symbol.iterator]() {
        return {
          next () {
            row = [...row.map(nextRow), 1]
            return row.length > index
              ? { done: true }
              : { value: row }
          }
        }
      }
    })
    this._lastRow = this.rows.slice(-1)[0]
  }

  get rows () {
    return this._rows
  }

  get lastRow () {
    return this._lastRow
  }
}
