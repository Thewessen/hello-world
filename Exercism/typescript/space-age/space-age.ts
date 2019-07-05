class SpaceAge {
  seconds: number
  EARTH: number

  constructor (time: number) {
    this.seconds = time
    this.EARTH = 31557600
  }

  onEarth(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH).toFixed(2))
  }

  onMercury(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH / 0.2408467).toFixed(2))
  }

  onVenus(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH / 0.61519726).toFixed(2))
  }

  onMars(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH / 1.8808158).toFixed(2))
  }

  onJupiter(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH / 11.862615).toFixed(2))
  }

  onSaturn(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH / 29.447498).toFixed(2))
  }

  onUranus(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH / 84.016846).toFixed(2))
  }

  onNeptune(): number {
    const { seconds, EARTH } = this
    return Number.parseFloat((seconds / EARTH / 164.79132).toFixed(2))
  }
}

export default SpaceAge
