'use strict'

export class BinarySearchTree {
  constructor (value) {
    this._data = value
    this._left = null
    this._right = null
  }

  get data() {
    return this._data
  }
  get right() {
    return this._right
  }

  get left() {
    return this._left
  }

  insert (value) {
    const dir = value <= this._data ? '_left' : '_right'
    if (this[dir] === null) {
      this[dir] = new BinarySearchTree(value)
    } else {
      this[dir].insert(value)
    }
  }

  each (fn) {
    if (this.left !== null) {
      this.left.each(fn)
    }
    fn(this.data)
    if (this.right !== null) {
      this.right.each(fn)
    }
  }
}
