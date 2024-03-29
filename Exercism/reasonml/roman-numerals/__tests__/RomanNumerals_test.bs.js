// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Jest = require("@glennsl/bs-jest/src/jest.js");
var RomanNumerals$RomanNumerals = require("../src/RomanNumerals.bs.js");

Jest.describe("RomanNumerals", (function (param) {
        Jest.test("1 is a single I", (function (param) {
                return Jest.Expect.toEqual("I", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(1)));
              }));
        Jest.test("2 is two I's", (function (param) {
                return Jest.Expect.toEqual("II", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(2)));
              }));
        Jest.test("3 is three I's", (function (param) {
                return Jest.Expect.toEqual("III", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(3)));
              }));
        Jest.test("4, being 5 - 1, is IV", (function (param) {
                return Jest.Expect.toEqual("IV", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(4)));
              }));
        Jest.test("5 is a single V", (function (param) {
                return Jest.Expect.toEqual("V", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(5)));
              }));
        Jest.test("6, being 5 + 1, is VI", (function (param) {
                return Jest.Expect.toEqual("VI", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(6)));
              }));
        Jest.test("9, being 10 - 1, is IX", (function (param) {
                return Jest.Expect.toEqual("IX", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(9)));
              }));
        Jest.test("20 is two X's", (function (param) {
                return Jest.Expect.toEqual("XXVII", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(27)));
              }));
        Jest.test("48 is not 50 - 2 but rather 40 + 8", (function (param) {
                return Jest.Expect.toEqual("XLVIII", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(48)));
              }));
        Jest.test("49 is not 40 + 5 + 4 but rather 50 - 10 + 10 - 1", (function (param) {
                return Jest.Expect.toEqual("XLIX", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(49)));
              }));
        Jest.test("50 is a single L", (function (param) {
                return Jest.Expect.toEqual("LIX", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(59)));
              }));
        Jest.test("90, being 100 - 10, is XC", (function (param) {
                return Jest.Expect.toEqual("XCIII", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(93)));
              }));
        Jest.test("100 is a single C", (function (param) {
                return Jest.Expect.toEqual("CXLI", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(141)));
              }));
        Jest.test("60, being 50 + 10, is LX", (function (param) {
                return Jest.Expect.toEqual("CLXIII", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(163)));
              }));
        Jest.test("400, being 500 - 100, is CD", (function (param) {
                return Jest.Expect.toEqual("CDII", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(402)));
              }));
        Jest.test("500 is a single D", (function (param) {
                return Jest.Expect.toEqual("DLXXV", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(575)));
              }));
        Jest.test("900, being 1000 - 100, is CM", (function (param) {
                return Jest.Expect.toEqual("CMXI", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(911)));
              }));
        Jest.test("1000 is a single M", (function (param) {
                return Jest.Expect.toEqual("MXXIV", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(1024)));
              }));
        return Jest.test("3000 is three M's", (function (param) {
                      return Jest.Expect.toEqual("MMM", Jest.Expect.expect(RomanNumerals$RomanNumerals.toRoman(3000)));
                    }));
      }));

/*  Not a pure module */
