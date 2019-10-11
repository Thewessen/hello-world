'use strict'

const isObject = (obj) => typeof(obj) === 'object' && obj !== null
const isNode = (node) => isObject(node) &&
  ['value', 'left', 'right'].every(prop => node.hasOwnProperty(prop))

// TODO: Make this Zipper immutable
// Could we do this differently?
const deepCopy = (tree) => {
  const newTree = {}
  for (const [key, value] of Object.entries(tree)) {
    if(isObject(value)) {
      newTree[key] = deepCopy(value)
    } else {
      newTree[key] = value
    }
  }
  return newTree
}

export class Zipper {
  constructor (focus, parent = null) {
    this.parent = parent
    this.focus = focus
  }

  static fromTree (tree) {
    if (!isNode(tree)) {
      throw new Error('Input is not a Binary Tree')
    }
    return new Zipper(deepCopy(tree))
  }

  toTree () {
    if (this.parent === null) {
      return this.focus
    }
    return this.parent.toTree()
  }

  left () {
    const { left } = this.focus
    return isNode(left) ? new Zipper(left, this) : null
  }

  right () {
    const { right } = this.focus
    return isNode(right) ? new Zipper(right, this) : null
  }

  value () {
    return this.focus.value
  }

  setValue (value) {
    this.focus.value = value
    return this
  }

  setLeft (node) {
    this.focus.left = isNode(node) ? deepCopy(node) : null
    return this
  }

  setRight (node) {
    this.focus.right = isNode(node) ? deepCopy(node) : null
    return this
  }

  up () {
    return this.parent
  }
}
