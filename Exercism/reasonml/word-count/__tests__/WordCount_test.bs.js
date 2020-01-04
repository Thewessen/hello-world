// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Jest = require("@glennsl/bs-jest/src/jest.js");
var Js_dict = require("bs-platform/lib/js/js_dict.js");
var WordCount$WordCount = require("../src/WordCount.bs.js");

Jest.describe("Word Count", (function (param) {
        Jest.test("count one word", (function (param) {
                var expected = Js_dict.fromArray(/* array */[/* tuple */[
                        "word",
                        1
                      ]]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("word")));
              }));
        Jest.test("multiple occurrences of a word", (function (param) {
                var expected = Js_dict.fromArray(/* array */[
                      /* tuple */[
                        "one",
                        1
                      ],
                      /* tuple */[
                        "fish",
                        4
                      ],
                      /* tuple */[
                        "two",
                        1
                      ],
                      /* tuple */[
                        "red",
                        1
                      ],
                      /* tuple */[
                        "blue",
                        1
                      ]
                    ]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("one fish two fish red fish blue fish")));
              }));
        Jest.test("handles expanded lists", (function (param) {
                var expected = Js_dict.fromArray(/* array */[
                      /* tuple */[
                        "one",
                        1
                      ],
                      /* tuple */[
                        "two",
                        1
                      ],
                      /* tuple */[
                        "three",
                        1
                      ]
                    ]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("one,\ntwo,\nthree")));
              }));
        Jest.test("ignore punctuation", (function (param) {
                var expected = Js_dict.fromArray(/* array */[
                      /* tuple */[
                        "car",
                        1
                      ],
                      /* tuple */[
                        "carpet",
                        1
                      ],
                      /* tuple */[
                        "as",
                        1
                      ],
                      /* tuple */[
                        "java",
                        1
                      ],
                      /* tuple */[
                        "javascript",
                        1
                      ]
                    ]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("car: carpet as java: javascript!!&@$%^&")));
              }));
        Jest.test("include numbers", (function (param) {
                var expected = Js_dict.fromArray(/* array */[
                      /* tuple */[
                        "1",
                        1
                      ],
                      /* tuple */[
                        "2",
                        1
                      ],
                      /* tuple */[
                        "testing",
                        2
                      ]
                    ]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("testing, 1, 2 testing")));
              }));
        Jest.test("normalize case", (function (param) {
                var expected = Js_dict.fromArray(/* array */[
                      /* tuple */[
                        "go",
                        3
                      ],
                      /* tuple */[
                        "stop",
                        2
                      ]
                    ]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("go Go GO Stop stop")));
              }));
        Jest.test("with apostrophes", (function (param) {
                var expected = Js_dict.fromArray(/* array */[
                      /* tuple */[
                        "first",
                        1
                      ],
                      /* tuple */[
                        "don't",
                        2
                      ],
                      /* tuple */[
                        "laugh",
                        1
                      ],
                      /* tuple */[
                        "then",
                        1
                      ],
                      /* tuple */[
                        "cry",
                        1
                      ]
                    ]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("First: don't laugh. Then: don't cry.")));
              }));
        Jest.test("with quotations", (function (param) {
                var expected = Js_dict.fromArray(/* array */[
                      /* tuple */[
                        "joe",
                        1
                      ],
                      /* tuple */[
                        "can't",
                        1
                      ],
                      /* tuple */[
                        "tell",
                        1
                      ],
                      /* tuple */[
                        "between",
                        1
                      ],
                      /* tuple */[
                        "large",
                        2
                      ],
                      /* tuple */[
                        "and",
                        1
                      ]
                    ]);
                return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount("Joe can't tell between 'large' and large.")));
              }));
        return Jest.test("multiple spaces not detected as a word", (function (param) {
                      var expected = Js_dict.fromArray(/* array */[
                            /* tuple */[
                              "multiple",
                              1
                            ],
                            /* tuple */[
                              "whitespaces",
                              1
                            ]
                          ]);
                      return Jest.Expect.toEqual(expected, Jest.Expect.expect(WordCount$WordCount.wordCount(" multiple   whitespaces")));
                    }));
      }));

/*  Not a pure module */
