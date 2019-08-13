'use strict'

const isNode = (node) => typeof(node) === 'object' && node !== null &&
  ['value', 'left', 'right'].every(prop => node.hasOwnProperty(prop))

class BinTree {
  constructor (value, parent, children) {
    this.value = value
    this.parent = parent
    this.children = children || []
  }
}

export class Zipper {
  constructor (root, focus, parent = null) {
    this.root = root
    this.focus = focus || root
    this.parent = parent ? new Zipper(
      root,
      parent,
      parent instanceof Zipper ? parent.parent : null
    ) : null
  }

  static fromTree (tree) {
    if (!isNode(tree)) {
      throw new Error('Input is not a Binary Tree')
    }
    return new Zipper(tree)
  }

  toTree () {
    return this.root
  }

  left () {
    const { left } = this.focus
    return isNode(left) ? new Zipper(this.root, left, this.focus) : null
  }

  right () {
    const { right } = this.focus
    return isNode(right) ? new Zipper(this.root, right, this.focus) : null
  }

  value () {
    return this.focus.value
  }

  setValue (value) {
    this.focus.value = value
    return this
  }

  setLeft (node) {
    this.focus.left = Object.assign(this.focus, node)
    return this
  }

  setRight (value) {
    this.focus.right = isNode(value) ? value : null
    return this
  }

  up () {
    return this.parent === null ? null : new Zipper(this.root, this.parent.focus, this.parent.parent)
  }
}

// function bt(value, left, right) {
//   return {
//     value,
//     left,
//     right,
//   };
// }

// function leaf(value) {
//   return bt(value, null, null);
// }

// const t1 = bt(1, bt(2, null, leaf(3)), leaf(4));
// const t2 = bt(1, bt(5, null, leaf(3)), leaf(4));
// const t3 = bt(1, bt(2, leaf(5), leaf(3)), leaf(4));
// const t4 = bt(1, leaf(2), leaf(4));
// const t5 = bt(1, bt(2, null, leaf(3)), bt(6, leaf(7), leaf(8)));
// const t6 = bt(1, bt(2, null, leaf(5)), leaf(4));
// const z = Zipper.fromTree(t1)
// console.log(z.root)
// z.focus = z.root.left
// console.log(z.root)
// console.log(z.focus)

