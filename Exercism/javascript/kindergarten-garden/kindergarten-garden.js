'use strict'

const STUDENTS = ['Alice', 'Bob', 'Charlie', 'David',
                  'Eve', 'Fred', 'Ginny', 'Harriet',
                  'Ileana', 'Joseph', 'Kincaid', 'Larry']

const PLANTS = new Map()
  .set('C', 'clover')
  .set('G', 'grass')
  .set('R', 'radishes')
  .set('V', 'violets')

export class Garden {
  constructor(diagram, students = STUDENTS) {
    students.sort()
    diagram.split('\n')
      .map(row => row.match(/.{2}/g))
      .reduce((row1, row2) => row1
        .map((plants, i) => [...plants, ...row2[i]]
          .map(plant => PLANTS.get(plant))))
      .forEach((garden, i) => this[students[i].toLowerCase()] = garden)
  }
}
