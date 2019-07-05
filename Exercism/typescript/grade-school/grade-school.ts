interface DB = {
  [grade: number]: string[]
}

class GradeSchool {
  private db: string[][]

  constructor () {
    this.db = []
  }

  roster (): DB {
    return {
      ...this.db.map((e) => [...e.sort()])
    }
  }

  add (student: string, grade: number) {
    const grade = this.db[grade] || []
    this.db[grade] = [...grade, student]
  }

  grade (grade: number): string[] {
    const grade = this.db[grade] || []
    return [...grade.sort()]
  }
}

export default GradeSchool
