type Color = 'black' | 'brown' | 'red'    | 'orange' | 'yellow' |
             'green' | 'blue'  | 'violet' | 'grey'   | 'white'

export class ResistorColor {
  static COLORS = new Map([
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
  ].map((e, i) => [e, i]))

  constructor(private colors: Color[]) {
    if (colors.length < 2) {
      throw new Error("At least two colors need to be present")
    }
  }

  value = (): number => Number(this.colors.slice(0, 2).map(c =>
    ResistorColor.COLORS.get(c)).join('')) ;
}
