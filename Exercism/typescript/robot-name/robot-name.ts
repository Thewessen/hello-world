type NameGenerator = Generator<string, string, void>
interface PartNameFunc {
  (char: string): NameGenerator
}
interface NameFunc {
  (): NameGenerator
}

const strArray = (from: string, too: string): string[] => {
  const [start, end] = [from, too]
    .map((e, i) => e.charCodeAt(0) + i)
  return Array.from(
    { length: end - start },
    (__, i) => String.fromCharCode(start + i)
  )
}

const rInt = (from: number, to: number): number =>
  Math.floor((Math.random() * (to - from) + from))

const prepend = (genNames: NameFunc): PartNameFunc  =>
  function * (char: string): NameGenerator {
    for (const name of genNames()) {
      yield name + char
    }
    return ''
  }

const combine = (gen: NameFunc, chars: string[]): NameFunc =>
  function * (): NameGenerator {
    const iters = chars.map(prepend(gen))
    const values = iters.map((iter) => iter.next().value)
    while (values.length > 0) {
      const i = rInt(0, values.length)
      yield values[i]
      const { value, done } = iters[i].next()
      if (done) {
        iters.splice(i, 1)
        values.splice(i, 1)
      } else {
        values[i] = value
      }
    }
    return ''
  }

const uniqueNames = (...template: string[][]): NameGenerator =>
  template.reduce(combine,
    function* () { yield ''; return '' })()

export default class Robot {
  private _name = ''
  static names: NameGenerator
  static template = [
    strArray('A', 'Z'),
    strArray('A', 'Z'),
    strArray('0', '9'),
    strArray('0', '9'),
    strArray('0', '9')
  ]
  constructor () {
    this.generateName()
  }

  resetName (): void {
    this.generateName()
  }

  get name (): string {
    return this._name
  }

  generateName (): void {
    const { value, done } = Robot.names.next()
    if (done) {
      throw new Error('No more Robots for you!')
    }
    this._name = value
  }

  static releaseNames(): void {
    Robot.names = uniqueNames(...Robot.template)
  }
}

Robot.releaseNames()
