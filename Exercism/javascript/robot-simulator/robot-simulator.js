'use strict'

export class InvalidInputError extends Error {}

export class Robot {
  constructor () {
    this.moves = new Map()
      .set('north', [0, 1])
      .set('east', [1, 0])
      .set('south', [0, -1])
      .set('west', [-1, 0])
    this.bearing = 'north'
    this.coordinates = [0, 0]
  }

  static instructions (string) {
    return [...string]
      .map(char => Robot.instruct.get(char))
  }

  orient (direction) {
    if (![...this.moves.keys()].includes(direction)) {
      throw new InvalidInputError()
    }
    this.bearing = direction
  }

  turn (directions) {
    this.bearing = directions[(directions.indexOf(this.bearing) + 1) % directions.length]
  }

  turnRight () {
    this.turn([...this.moves.keys()])
  }

  turnLeft () {
    this.turn([...this.moves.keys()].reverse())
  }

  at (...coords) {
    this.coordinates = coords
  }

  advance () {
    const [dx, dy] = this.moves.get(this.bearing)
    const [x, y] = this.coordinates
    this.coordinates = [x + dx, y + dy]
  }

  place ({x, y, direction}) {
    this.coordinates = [x, y]
    this.bearing = direction
  }

  evaluate (string) {
    Robot.instructions(string)
      .forEach(fn => this[fn]())
  }
}

Robot.instruct = new Map()
  .set('A', 'advance')
  .set('R', 'turnRight')
  .set('L', 'turnLeft')
