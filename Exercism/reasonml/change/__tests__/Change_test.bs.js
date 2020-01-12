// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Jest = require("@glennsl/bs-jest/src/jest.js");
var Change$Change = require("../src/Change.bs.js");

Jest.describe("Change", (function (param) {
        Jest.test("single coin change", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            25,
                            /* [] */0
                          ], Jest.Expect.expect(Change$Change.makeChange(25, /* :: */[
                                    1,
                                    /* :: */[
                                      5,
                                      /* :: */[
                                        10,
                                        /* :: */[
                                          25,
                                          /* :: */[
                                            100,
                                            /* [] */0
                                          ]
                                        ]
                                      ]
                                    ]
                                  ])));
              }));
        Jest.test("multiple coin change", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            5,
                            /* :: */[
                              10,
                              /* [] */0
                            ]
                          ], Jest.Expect.expect(Change$Change.makeChange(15, /* :: */[
                                    1,
                                    /* :: */[
                                      5,
                                      /* :: */[
                                        10,
                                        /* :: */[
                                          25,
                                          /* :: */[
                                            100,
                                            /* [] */0
                                          ]
                                        ]
                                      ]
                                    ]
                                  ])));
              }));
        Jest.test("change with Lilliputian Coins", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            4,
                            /* :: */[
                              4,
                              /* :: */[
                                15,
                                /* [] */0
                              ]
                            ]
                          ], Jest.Expect.expect(Change$Change.makeChange(23, /* :: */[
                                    1,
                                    /* :: */[
                                      4,
                                      /* :: */[
                                        15,
                                        /* :: */[
                                          20,
                                          /* :: */[
                                            50,
                                            /* [] */0
                                          ]
                                        ]
                                      ]
                                    ]
                                  ])));
              }));
        Jest.test("change with Lower Elbonia Coins", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            21,
                            /* :: */[
                              21,
                              /* :: */[
                                21,
                                /* [] */0
                              ]
                            ]
                          ], Jest.Expect.expect(Change$Change.makeChange(63, /* :: */[
                                    1,
                                    /* :: */[
                                      5,
                                      /* :: */[
                                        10,
                                        /* :: */[
                                          21,
                                          /* :: */[
                                            25,
                                            /* [] */0
                                          ]
                                        ]
                                      ]
                                    ]
                                  ])));
              }));
        Jest.test("large target values", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            2,
                            /* :: */[
                              2,
                              /* :: */[
                                5,
                                /* :: */[
                                  20,
                                  /* :: */[
                                    20,
                                    /* :: */[
                                      50,
                                      /* :: */[
                                        100,
                                        /* :: */[
                                          100,
                                          /* :: */[
                                            100,
                                            /* :: */[
                                              100,
                                              /* :: */[
                                                100,
                                                /* :: */[
                                                  100,
                                                  /* :: */[
                                                    100,
                                                    /* :: */[
                                                      100,
                                                      /* :: */[
                                                        100,
                                                        /* [] */0
                                                      ]
                                                    ]
                                                  ]
                                                ]
                                              ]
                                            ]
                                          ]
                                        ]
                                      ]
                                    ]
                                  ]
                                ]
                              ]
                            ]
                          ], Jest.Expect.expect(Change$Change.makeChange(999, /* :: */[
                                    1,
                                    /* :: */[
                                      2,
                                      /* :: */[
                                        5,
                                        /* :: */[
                                          10,
                                          /* :: */[
                                            20,
                                            /* :: */[
                                              50,
                                              /* :: */[
                                                100,
                                                /* [] */0
                                              ]
                                            ]
                                          ]
                                        ]
                                      ]
                                    ]
                                  ])));
              }));
        Jest.test("possible change without unit coins available", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            2,
                            /* :: */[
                              2,
                              /* :: */[
                                2,
                                /* :: */[
                                  5,
                                  /* :: */[
                                    10,
                                    /* [] */0
                                  ]
                                ]
                              ]
                            ]
                          ], Jest.Expect.expect(Change$Change.makeChange(21, /* :: */[
                                    2,
                                    /* :: */[
                                      5,
                                      /* :: */[
                                        10,
                                        /* :: */[
                                          20,
                                          /* :: */[
                                            50,
                                            /* [] */0
                                          ]
                                        ]
                                      ]
                                    ]
                                  ])));
              }));
        Jest.test("another possible change without unit coins available", (function (param) {
                return Jest.Expect.toEqual(/* :: */[
                            4,
                            /* :: */[
                              4,
                              /* :: */[
                                4,
                                /* :: */[
                                  5,
                                  /* :: */[
                                    5,
                                    /* :: */[
                                      5,
                                      /* [] */0
                                    ]
                                  ]
                                ]
                              ]
                            ]
                          ], Jest.Expect.expect(Change$Change.makeChange(27, /* :: */[
                                    4,
                                    /* :: */[
                                      5,
                                      /* [] */0
                                    ]
                                  ])));
              }));
        Jest.test("no coins make 0 change", (function (param) {
                return Jest.Expect.toEqual(/* [] */0, Jest.Expect.expect(Change$Change.makeChange(0, /* :: */[
                                    1,
                                    /* :: */[
                                      5,
                                      /* :: */[
                                        10,
                                        /* :: */[
                                          21,
                                          /* :: */[
                                            25,
                                            /* [] */0
                                          ]
                                        ]
                                      ]
                                    ]
                                  ])));
              }));
        Jest.test("error testing for change smaller than the smallest of coins", (function (param) {
                return Jest.Expect.toEqual(undefined, Jest.Expect.expect(Change$Change.makeChange(3, /* :: */[
                                    5,
                                    /* :: */[
                                      10,
                                      /* [] */0
                                    ]
                                  ])));
              }));
        Jest.test("error if no combination can add up to target", (function (param) {
                return Jest.Expect.toEqual(undefined, Jest.Expect.expect(Change$Change.makeChange(94, /* :: */[
                                    5,
                                    /* :: */[
                                      10,
                                      /* [] */0
                                    ]
                                  ])));
              }));
        return Jest.test("cannot find negative change values", (function (param) {
                      return Jest.Expect.toEqual(undefined, Jest.Expect.expect(Change$Change.makeChange(-5, /* :: */[
                                          1,
                                          /* :: */[
                                            2,
                                            /* :: */[
                                              5,
                                              /* [] */0
                                            ]
                                          ]
                                        ])));
                    }));
      }));

/*  Not a pure module */
