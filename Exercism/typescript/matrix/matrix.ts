const zip = (...arrays: number[][]): number[][] => {
  const iters = arrays.map((array) => array[Symbol.iterator]())
  let items = iters.map((iter) => iter.next())
  const columns = []
  while (!items.some((item) => item.done)) {
    columns.push(items.map((item) => item.value))
    items = iters.map((iter) => iter.next())
  }
  return columns
}

class Matrix {
  rows: number[][]
  columns: number[][]

  constructor (matrix: string) {
    this.rows = matrix
      .split('\n')
      .map((row) => row.split(' ').map(Number))
    this.columns = zip(...this.rows)
  }
}

export default Matrix
