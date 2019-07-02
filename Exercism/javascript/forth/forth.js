'use strict'

const OPERATIONS = new Map([
  ['+', (a, b) => a + b],
  ['*', (a, b) => a * b],
  ['-', (a, b) => a - b],
  ['/', (a, b) => {
    if (b === 0) {
      throw new Error('Division by zero')
    }
    return Number.parseInt(a / b)
  }]
])

const MANIPU = new Map([
  ['DUP', (stack) => {
    if (stack.length === 0) {
      throw new Error('Stack empty')
    }
    return [...stack, ...stack.slice(-1)]
  }],
  ['DROP', (stack) => {
    if (stack.length === 0) {
      throw new Error('Stack empty')
    }
    return stack.slice(0, stack.length - 1)
  }],
  ['SWAP', (stack) => {
    if (stack.length < 2) {
      throw new Error('Stack empty')
    }
    return [
      ...stack.slice(0, stack.length - 2),
      ...stack.slice(-2).reverse()
    ]
  }],
  ['OVER', (stack) => {
    if (stack.length < 2) {
      throw new Error('Stack empty')
    }
    return [
      ...stack.slice(0, stack.length - 1),
      ...stack.slice(-2).reverse()
    ]
  }]
])

export class Forth {
  constructor () {
    this.stack = []
    this.custom = new Map()
  }

  evaluate (string) {
    const commands = string.split(' ')

    for (let cmd of commands) {
      cmd = cmd.toUpperCase()
      if (!isNaN(cmd)) {
        this.stack.push(Number(cmd))
      }
      else if (this.custom.has(cmd)) {
        this.evaluate(this.custom.get(cmd))
      }
      else if (OPERATIONS.has(cmd)) {
        if (this.stack.length < 2) {
          throw new Error('Stack empty')
        }
        this.stack = [
          ...this.stack.slice(0, this.stack.length - 2),
          OPERATIONS.get(cmd)(...this.stack.slice(-2))
        ]
      }
      else if (MANIPU.has(cmd)) {
        this.stack = MANIPU.get(cmd)(this.stack)
      }
      else if (cmd === ':') {
        if (!isNaN(commands[1])) {
          throw new Error('Invalid definition')
        }
        this.custom.set(
          commands[1].toUpperCase(),
          commands.slice(2, commands.length -1).join(' ')
        )
        break
      }
      else {
        throw new Error('Unknown command')
      }
    }
  }
}
