'use strict'

const isNode = (node) => typeof(node) === 'object' && node !== null &&
  ['value', 'left', 'right'].every(prop => node.hasOwnProperty(prop))

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
    let node = this
    while(node.parent !== null) {
      node = node.up()
    }
    return this.focus
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
    this.focus.value = value
    return this
  }

  setLeft (node) {
    this.focus.left = isNode(node) ? Object.assign({}, node) : null
    return this
  }

  setRight (node) {
    this.focus.right = isNode(node) ? Object.assign({}, node) : null
    return this
  }

  up () {
    return this.parent === null ? this : this.parent
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
// // const t2 = bt(1, bt(5, null, leaf(3)), leaf(4));
// const t3 = bt(1, bt(2, leaf(5), leaf(3)), leaf(4));
// const t4 = bt(1, leaf(2), leaf(4));
// const t5 = bt(1, bt(2, null, leaf(3)), bt(6, leaf(7), leaf(8)));
// const t6 = bt(1, bt(2, null, leaf(5)), leaf(4));
// let z = Zipper.fromTree(t1)
// console.log(z.left().setLeft(leaf(5)).toTree())
// console.log(t3)
// z = Zipper.fromTree(t1)
// console.log(z.left().setRight(null).toTree())
// console.log(t4)
// console.log(z.parent)
// z.focus = z.parent.left
// console.log(z.parent)
// console.log(z.focus)

