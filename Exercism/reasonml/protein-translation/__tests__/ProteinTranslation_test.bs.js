// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Jest = require("@glennsl/bs-jest/src/jest.js");
var ProteinTranslation$ProteinTranslation = require("../src/ProteinTranslation.bs.js");

Jest.describe("Protein Translation", (function (param) {
        Jest.test("Methionine RNA sequence", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Methionine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("AUG")));
              }));
        Jest.test("Phenylalanine RNA sequence 1", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Phenylalanine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UUU")));
              }));
        Jest.test("Phenylalanine RNA sequence 2", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Phenylalanine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UUC")));
              }));
        Jest.test("Leucine RNA sequence 1", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Leucine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UUA")));
              }));
        Jest.test("Leucine RNA sequence 2", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Leucine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UUG")));
              }));
        Jest.test("Serine RNA sequence 1", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Serine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UCU")));
              }));
        Jest.test("Serine RNA sequence 2", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Serine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UCC")));
              }));
        Jest.test("Serine RNA sequence 3", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Serine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UCA")));
              }));
        Jest.test("Serine RNA sequence 4", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Serine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UCG")));
              }));
        Jest.test("Tyrosine RNA sequence 1", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Tyrosine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UAU")));
              }));
        Jest.test("Tyrosine RNA sequence 2", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Tyrosine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UAC")));
              }));
        Jest.test("Cysteine RNA sequence 1", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Cysteine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UGU")));
              }));
        Jest.test("Cysteine RNA sequence 2", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Cysteine",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UGC")));
              }));
        Jest.test("Tryptophan RNA sequence", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Tryptophan",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UGG")));
              }));
        Jest.test("STOP codon RNA sequence 1", (function (param) {
                return Jest.Expect.toEqual(/* [] */0, Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UAA")));
              }));
        Jest.test("STOP codon RNA sequence 2", (function (param) {
                return Jest.Expect.toEqual(/* [] */0, Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UAG")));
              }));
        Jest.test("STOP codon RNA sequence 3", (function (param) {
                return Jest.Expect.toEqual(/* [] */0, Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UGA")));
              }));
        Jest.test("Translate RNA strand into correct protein list", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Methionine",
                            /* :: */[
                              "Phenylalanine",
                              /* :: */[
                                "Tryptophan",
                                /* [] */0
                              ]
                            ]
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("AUGUUUUGG")));
              }));
        Jest.test("Translation stops if STOP codon at beginning of sequence", (function (param) {
                return Jest.Expect.toEqual(/* [] */0, Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UAGUGG")));
              }));
        Jest.test("Translation stops if STOP codon at end of two-codon sequence", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Tryptophan",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UGGUAG")));
              }));
        Jest.test("Translation stops if STOP codon at end of three-codon sequence", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Methionine",
                            /* :: */[
                              "Phenylalanine",
                              /* [] */0
                            ]
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("AUGUUUUAA")));
              }));
        Jest.test("Translation stops if STOP codon in middle of three-codon sequence", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            "Tryptophan",
                            /* [] */0
                          ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UGGUAGUGG")));
              }));
        return Jest.test("Translation stops if STOP codon in middle of six-codon sequence", (function (param) {
                      return Jest.Expect.toEqual(/* :: */[
                                  "Tryptophan",
                                  /* :: */[
                                    "Cysteine",
                                    /* :: */[
                                      "Tyrosine",
                                      /* [] */0
                                    ]
                                  ]
                                ], Jest.Expect.expect(ProteinTranslation$ProteinTranslation.proteins("UGGUGUUAUUAAUGGUUU")));
                    }));
      }));

/*  Not a pure module */
