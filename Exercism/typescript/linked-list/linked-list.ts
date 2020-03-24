class LinkNode<T> {
  constructor (
    private value: T,
    private previous: LinkNode<T> | null = null,
    private next: LinkNode<T> | null = null,
  ) {}
  
  getValue (): T {
    return this.value
  }

  getPrevious (): LinkNode<T> | null {
    return this.previous
  }

  setPrevious (value: LinkNode<T> | null): void {
    this.previous = value
  }

  getNext (): LinkNode<T> | null {
    return this.next
  }

  setNext (value: LinkNode<T> | null): void {
    this.next = value
  }
}

export default class LinkedList<T> {
  constructor (
    private head: LinkNode<T> | null = null,
  ) {}

  last (): LinkNode<T> | null {
    let lastNode = this.head
    while (
      lastNode instanceof LinkNode &&
      lastNode.getNext() instanceof LinkNode
    ) {
      lastNode = lastNode.getNext()
    }
    return lastNode
  }

  push (value: T): void {
    const lastNode = this.last()
    if (lastNode instanceof LinkNode) {
      lastNode.setNext(new LinkNode(value, lastNode, null))
    } else {
      this.head = new LinkNode(value, null, null)
    }
  }

  pop (): T {
    const lastNode = this.last()
    if (lastNode === null) {
      throw new Error('Empty list!')
    }
    const previous = lastNode.getPrevious()
    if (previous instanceof LinkNode) {
      previous.setNext(null)
    }
    return lastNode.getValue()
  }

  shift (): T {
    const firstNode = this.head
    if (firstNode === null) {
      throw new Error('List empty!')
    }

    const next = firstNode.getNext()
    if (next instanceof LinkedList) {
      next.setPrevious(null)
    }

    this.head = next
    return firstNode.getValue()
  }

  unshift (value: T): void {
    const newNode = new LinkNode(value, null, this.head)
    if (this.head instanceof LinkNode) {
      this.head.setPrevious(newNode)
    }
    this.head = newNode
  }

  count(): number {
    let count = 0
    let node = this.head
    while (node instanceof LinkNode) {
      count += 1
      node = node.getNext()
    }
    return count
  }
  // delete (value) {
  //   const index = this.data.map(
  //       (node) => node.value
  //     ).indexOf(value)
  //   if (index >= 0) {
  //     const node = this.data.splice(index, 1)[0]
  //     if (node.before !== null) {
  //       this.data[index - 1].after = node.after
  //     }
  //     if (node.after !== null) {
  //       this.data[index].before = node.before
  //     }
  //     return this.data.length
  //   }
  // }
}
