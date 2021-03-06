// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Jest = require("@glennsl/bs-jest/src/jest.js");
var Acronym$Acronym = require("../src/Acronym.bs.js");

Jest.describe("Acronym", (function (param) {
        Jest.test("basic", (function (param) {
                return Jest.Expect.toEqual("PNG", Jest.Expect.expect(Acronym$Acronym.abbreviate("Portable Network Graphics")));
              }));
        Jest.test("lowercase words", (function (param) {
                return Jest.Expect.toEqual("ROR", Jest.Expect.expect(Acronym$Acronym.abbreviate("Ruby on Rails")));
              }));
        Jest.test("punctuation", (function (param) {
                return Jest.Expect.toEqual("FIFO", Jest.Expect.expect(Acronym$Acronym.abbreviate("First In, First Out")));
              }));
        Jest.test("all caps word", (function (param) {
                return Jest.Expect.toEqual("GIMP", Jest.Expect.expect(Acronym$Acronym.abbreviate("GNU Image Manipulation Program")));
              }));
        return Jest.test("punctuation without whitespace", (function (param) {
                      return Jest.Expect.toEqual("CMOS", Jest.Expect.expect(Acronym$Acronym.abbreviate("Complementary metal-oxide semiconductor")));
                    }));
      }));

/*  Not a pure module */
