'use strict'

export class GradeSchool {
  constructor () {
    this._db = []
  }

  roster () {
    return {
      ...this._db.map((e) => [...e.sort()])
    }
  }

  add (student, grade) {
    let _grade = this._db[grade] || []
    this._db[grade] = [..._grade, student]
  }

  grade (grade) {
    let _grade = this._db[grade] || []
    return [..._grade.sort()]
  }
}
