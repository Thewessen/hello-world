'use strict'

const isPrime = (p) => {
  return [...Array(Math.floor(Math.sqrt(p))).keys()]
    .slice(2)
    .every(n => p % n)
}

export class DiffieHellman {
  constructor (p, q) {
    if (!isPrime(p) || !isPrime(q)) {
      throw new Error('p and q should be primes')
    }
    this.p = p
    this.q = q
  }

  testKey (key) {
    if (!Number.isInteger(key) || key <= 1 || key >= this.p) {
      return false
    }
    return true
  }

  getPublicKeyFromPrivateKey(privateKey) {
    if (!this.testKey(privateKey)) {
      throw new Error('Invalid private key')
    }
    return this.q ** privateKey % this.p
  }

  getSharedSecret (privateKey, publicKey) {
    if (!this.testKey(privateKey)) {
      throw new Error('Invalid private key')
    }
    if (!this.testKey(publicKey)) {
      throw new Error('Invalid public key')
      
    }
    return publicKey ** privateKey % this.p
  }
}
