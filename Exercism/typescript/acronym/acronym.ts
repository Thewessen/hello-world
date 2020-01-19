export default class Acronym {
  public static parse(phrase: string): string {
    const acronym = phrase.match(/([A-Z](?=[a-z]+)|\b\w)/g)
    return acronym !== null
      ? acronym.join('').toUpperCase()
      : ''
  }
}
