export const abilityModifier = (constitution) => {
  if (constitution > 18) {
    throw new Error('Ability scores can be at most 18')
  }
  if (constitution < 3) {
    throw new Error('Ability scores must be at least 3')
  }
  return Math.floor((constitution - 10) / 2) 
}


export class Character {
  static rollAbility() {
    return Array.from({length: 4}, () => Math.floor(Math.random() * 6) + 1)
      .sort()
      .slice(1)
      .reduce((a, b) => a + b)
  }

  constructor () {
    this.strength = Character.rollAbility()
    this.dexterity = Character.rollAbility()
    this.constitution = Character.rollAbility()
    this.intelligence = Character.rollAbility()
    this.wisdom = Character.rollAbility()
    this.charisma = Character.rollAbility()
  }

  get hitpoints() {
    return 10 + abilityModifier(this.constitution)
  }
}
