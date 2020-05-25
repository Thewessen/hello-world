{
  // Write the type for assign with 2, 3, 4, 5 arguments
function assign<A, B, C, D, E>(o1: A, o2: B, o3: C, o4: D, o5: E): A & B & C & D & E
function assign<A, B, C, D>(o1: A, o2: B, o3: C, o4: D): A & B & C & D
function assign<A, B, C>(o1: A, o2: B, o3: C): A & B & C
function assign<A, B>(o1: A, o2: B): A & B
function assign<A>(o1: A): A
function assign(...objects: any[]): any {
    throw "Not implemented" // ignore this line
  }

  {
    // Ok
    const x = assign({ a: 1, b: 2}, { b: 2, c: false}, { e: 3 })

    x.a = 3
    x.b = 3
    x.c = false
    x.e = 2

    assign({ a: 1, b: 2}, { b: 2, c: false}, { e: 3 }, {}, { z: true })

    // Not ok
    assign({ x: 0 })
    x.d = 1
    x.c = "test"
  }
}
