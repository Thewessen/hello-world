type A = {
  title: string
  subtitle?: string
}

type B = {
  name: string
  age: number
}

const C: A & B = {
  title: "Making typescript exercises",
  subtitle: "doing ok...",
  name: "Samuel",
  age: 60
}
