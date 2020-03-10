'use strict'

const count = head => {
  const h = head()
  return () => ({
    head: () => h,
    tail: count(() => h + 1)
  })
}

const toArray = list => {
  const l = list()
  if (l === null) return []
  return [l.head(), ...toArray(l.tail)]
}

const filter = (fn, list) => {
  const l = list()
  if (l === null) return null

  const h = l.head()
  return fn(h)
    ? () => ({
      head: () => h,
      tail: filter(fn, l.tail)
    })
    : filter(fn, l.tail)
}

const takeWhile = (fn, list) => {
  const l = list()
  if (l === null) return null

  const h = l.head()
  return fn(h)
    ? () => ({
        head: () => h,
        tail: takeWhile(fn, l.tail)
      })
    : () => null
}

const sieve = list => {
  const l = list()
  if (l === null) return null

  const h = l.head()
  return () => ({
    head: () => h,
    tail: sieve(filter(n => n % h, l.tail))
  })
}

const primes = till => toArray(
  takeWhile(n => n <= till, sieve(count(() => 2)))
)

const printList = list => {
  let l = list()
  while (l !== null) {
    console.log(l.head())
    l = l.tail()
  }
}


printList(sieve(count(() => 2)))
