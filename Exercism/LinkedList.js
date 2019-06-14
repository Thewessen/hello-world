'use strict'

// Implement a doubly linked list.
// Like an array, a linked list is a simple linear data structure.
// Several common data types can be implemented using linked lists, like queues, stacks, and associative arrays.
// A linked list is a collection of data elements called nodes.
// In a singly linked list each node holds a value and a link to the next node.
// In a doubly linked list each node also holds a link to the previous node.
// You will write an implementation of a doubly linked list.
// Implement a Node to hold a value and pointers to the next and previous nodes.
// Then implement a List which holds references to the first and last node and
// offers an array-like interface for adding and removing items: push (insert
// value at back); pop (remove value at back); shift (remove value at front).
// unshift (insert value at front); To keep your implementation simple, the
// tests will not cover error conditions.  Specifically: pop or shift will
// never be called on an empty list.

const lastElement = (arr) => arr[arr.length - 1]

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
      .map((e, i) => new LinkNode(...[
          e,
          i - 1 >= 0 ? data[i - 1] : null,
          i + 1 <= data.length ? data[i + 1] : null
        ])
      )
  }

  push (value) {
    lastElement(data).after = value
    this.data.push(new LinkedList(
      value,
      lastElement(data).value,
      null,
    ))
    return value
  }

  pop (index) {
    const node = this.data.pop(index)
    if(index < this.data.length) {
      this.data[index].before = node.before
    }
    return node
  }

}

// module.exports = LinkedList
const myarr = new LinkedList('samuel')
console.log(myarr)
