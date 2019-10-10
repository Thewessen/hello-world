'use strict'

const isNode = (node) => typeof(node) === 'object' && node !== null &&
  ['value', 'left', 'right'].every(prop => node.hasOwnProperty(prop))

// TODO: Make this Zipper immutable
export class Zipper {
  constructor (parent, focus) {
    this.parent = parent
    this.focus = focus
  }

  static fromTree (tree) {
    if (!isNode(tree)) {
      throw new Error('Input is not a Binary Tree')
    }
    return new Zipper(null, tree)
  }

  toTree () {
    if (this.parent === null) {
      return this.focus
    }
    return this.parent.toTree()
  }

  left () {
    const { left } = this.focus
    return isNode(left) ? new Zipper(this, left) : null
  }

  right () {
    const { right } = this.focus
    return isNode(right) ? new Zipper(this, right) : null
  }

  value () {
    return this.focus.value
  }

  setValue (value) {
    // TODO: This works, but...
    // It changes t1 for the rest of the test.
    // Data should be immutable
    this.focus.value = value
    return this
  }

  setLeft (node) {
    this.focus.left = isNode(node) ? {...node} : null
    return this
  }

  setRight (node) {
    this.focus.right = isNode(node) ? {...node} : null
    return this
  }

  up () {
    return this.parent
  }
}
