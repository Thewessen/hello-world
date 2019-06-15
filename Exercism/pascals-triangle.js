'use strict'

class Triangle {
  constructor (index) {
    if (!Number.isInteger(index)) {
      return new Error('Constructor argument is not an integer')
    }
    let row = []
    const next = (e, i, arr) => {
                      let add = arr[i - 1] || 0
                      return e + add
                    }
    this._rows = Array.from({
      [Symbol.iterator]() {
        return {
          next () {
            row = [...row.map(next), 1]
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

module.exports = Triangle
