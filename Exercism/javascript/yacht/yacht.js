"use strict";

// Some helper functions
const count = (n, dice) => dice.filter(d => d == n).length;
const sum = arr => arr.reduce((a, b) => a + b);
const scr = n => dice => count(n, dice) * n;
const straight = from => dice =>
  dice.sort().every((d, i) => d === i + from) ? 30 : 0;

const CATEGORIES = new Map([
  ["yacht", dice => (new Set(dice)).size === 1 ? 50 : 0],
  ["ones", scr(1)],
  ["twos", scr(2)],
  ["threes", scr(3)],
  ["fours", scr(4)],
  ["fives", scr(5)],
  ["sixes", scr(6)],
  ["little straight", straight(1)],
  ["big straight", straight(2)],
  [
    "full house",
    dice =>
      dice.every(d => count(d, dice) === 2 || count(d, dice) === 3)
        ? sum(dice)
        : 0
  ],
  [
    "four of a kind",
    dice => {
      const n = dice.find(d => count(d, dice) === 4);
      typeof n !== "undefined" ? scr(n)(dice) : 0;
    }
  ],
  ["choice", dice => sum(dice)]
]);

export const score = (dice, category) => {
  if (
    dice.length !== 5 ||
    dice.some(d => d > 6) ||
    dice.some(d => d < 1) ||
    !CATEGORIES.has(category)
  ) {
    throw new Error("Something went wrong");
  }
  return CATEGORIES.get(category)(dice);
};
