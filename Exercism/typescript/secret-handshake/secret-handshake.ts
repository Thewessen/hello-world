export default class HandShake {
  private _commands = [
    'wink',
    'double blink',
    'close your eyes',
    'jump'
  ]

  constructor(private _value: number) {}

  commands() {
    const bin = this._value
      .toString(2)
      .split('')
      .map(Number)
      .reverse()

    const commands = this._commands
      .filter((_, i) => bin[i])

    return this._value & 0b10000
      ? commands.reverse()
      : commands
  }
}
