type Roster = Map<string, string[]>

class GradeSchool {
  private db: Roster = new Map()

  constructor () {}

  studentRoster (): Roster {
    const roster: Roster = new Map()
    for (const [g, s] of this.db.entries()) {
      roster.set(g, [...s])
    }
    return roster
  }

  addStudent (student: string, grade: number) {
    const g = this.db.get(String(grade)) || []
    this.db.set(String(grade), [...g, student].sort())
  }

  studentsInGrade (grade: number): string[] {
    const g = this.db.get(String(grade)) || []
    return [...g]
  }
}

export default GradeSchool
