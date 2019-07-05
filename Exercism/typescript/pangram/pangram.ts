class Pangram {
  text: string

  constructor (text: string = '') {
    this.text = text
  }

  isPangram = (): boolean =>
    new Set(this.text
      .toLowerCase()
      .match(/[a-z]/g)
    ).size === 26
}

export default Pangram
