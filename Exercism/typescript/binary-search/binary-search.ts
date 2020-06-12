const isSorted = (array: number[]): boolean => array.every(
  (e, i) => i === 0 || e >= array[i - 1]
)

export default class BinarySearch {
  constructor (private _data: number[]) {}

  get array(): number[] | undefined {
    if (Array.isArray(this._data) && isSorted(this._data)) {
      return this._data;
    }
  }

  indexOf(el: number, array = this.array): number {
    if (array === undefined || array.length === 0) {
      return -1
    }
    const mid = Math.trunc(array.length / 2)
    if (el === array[mid]) {
      return mid
    }
    if (el < array[mid]) {
      return this.indexOf(el, array.slice(0, mid))
    }
    const index = this.indexOf(el, array.slice(mid + 1))
    return index === -1
      ? index
      : mid + 1 + index
  }
}
