export default class Gigasecond {
  time: Date

  constructor (time: Date = new Date()) {
    this.time = time
  }

  date (): Date {
    return new Date(this.time.getTime() + 1e12)
  }
}
