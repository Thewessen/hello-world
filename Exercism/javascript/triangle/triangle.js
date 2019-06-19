'use strict'

const everyOther = (index, array) =>
  array.filter((el, idx) => idx !== index)

const allNumbers = (array) =>
  array.every((e) => Number.isFinite(e))

const allPositive = (array) =>
  array.every((e) => e > 0)

const hasThreeElements = (array) =>
  array.length === 3

const sumRule = (array) =>
  array.every((e, i, arr) =>
    e < everyOther(i, arr).reduce(
      (acc, curr) => acc + curr
    )
  )

const isTriangle = (array) => [
  hasThreeElements,
  allNumbers,
  allPositive,
  sumRule
].every((f) => f(array))

const equilateral = (triangle) =>
  triangle.every((x, i, arr) =>
    everyOther(i, arr).every(
      (y) => x === y
    )
  )

const isosceles = (triangle) =>
  triangle.some((x, i, arr) =>
    everyOther(i, arr).some(
      (y) => x === y
    )
  )

const scalene = (triangle) =>
  !isosceles(triangle)

const TYPES = [
  equilateral,
  isosceles,
  scalene
]

export class Triangle {
  constructor (...args) {
    this.triangle = args
  }

  kind () {
    if (!isTriangle(this.triangle)) {
      throw new Error('Not a triangle')
    }
    for (const type of TYPES) {
      if (type(this.triangle)) {
        return type.name
      }
    }
    throw new Error('Something went horribly wrong!')
  }
}
