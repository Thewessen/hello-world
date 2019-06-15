'use strict'

// Implement a doubly linked list.
// 
// Like an array, a linked list is a simple linear data structure.
// Several common data types can be implemented using linked lists,
// like queues, stacks, and associative arrays.
// 
// A linked list is a collection of data elements called nodes.
// In a singly linked list each node holds a value and a link to the next node.
// In a doubly linked list each node also holds a link to the previous node.
// 
// You will write an implementation of a doubly linked list.
// Implement a Node to hold a value and pointers to the next and previous nodes.
// Then implement a List which holds references to the first and last node and
// offers an array-like interface for adding and removing items:
// - push (insert value at back);
// - pop (remove value at back);
// - shift (remove value at front);
// - unshift (insert value at front);
// 
// To keep your implementation simple, the tests will not cover error conditions.
// Specifically: pop or shift will never be called on an empty list.

class LinkNode {
  constructor (value, before = null, after = null) {
    this.value = value
    this.before = before
    this.after = after
  }
}

class LinkedList {
  constructor (data) {
    if (!data[Symbol.iterator]) {
      return new Error('Data is not iterable')
    }
    this.data = Array.from(data)
      .map((e) => new LinkNode( e, null, null))
      .map((e, i, arr) => {
        e.before = i > 0 ? arr[i - 1] : null
        e.after = i < arr.length - 1 ? arr[i + 1] : null
        return e
      })
  }

  last () {
    if (this.data.length !== 0) {
      return this.data[this.data.length - 1]
    } else {
      return null
    }
  }

  first () {
    if (this.data.length !== 0) {
      return this.data[0]
    }
  }

  push (value) {
    const node = new LinkNode(
      value, this.last(), null
    )
    this.last().after = node
    this.data.push(node)
    return this.data.length
  }

  pop () {
    const node = this.data.pop()
    if (this.last()) {
      this.last().after = null
    }
    return node
  }

  shift () {
    const node = this.data.shift()
    if (this.data.length !== 0) {
      this.first().before = null
    }
    return node
  }

  unshift (value) {
    const node =  new LinkNode(
      value, null, this.first()
    )
    if (this.data.length !== 0) {
      this.first().before = node
    }
    this.data.unshift(node)
    return this.data.length
  }
}

module.exports = LinkedList
