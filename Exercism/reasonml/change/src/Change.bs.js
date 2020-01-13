// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var List = require("bs-platform/lib/js/list.js");
var $$Array = require("bs-platform/lib/js/array.js");
var Caml_array = require("bs-platform/lib/js/caml_array.js");
var Pervasives = require("bs-platform/lib/js/pervasives.js");

function min(a, b) {
  var match = List.length(a) < List.length(b);
  if (match) {
    return a;
  } else {
    return b;
  }
}

function makeChange(value, change) {
  var make = function (results, _param) {
    while(true) {
      var param = _param;
      if (param) {
        var coin = param[0];
        $$Array.iteri((function(coin){
            return function (i) {
              if (i !== 0) {
                if (i < coin) {
                  return (function (param) {
                      return /* () */0;
                    });
                } else {
                  return (function (r) {
                      var match = Caml_array.caml_array_get(results, i - coin | 0);
                      if (match !== undefined) {
                        var prev = match;
                        if (r !== undefined) {
                          return Caml_array.caml_array_set(results, i, min(Pervasives.$at(prev, /* :: */[
                                              coin,
                                              /* [] */0
                                            ]), r));
                        } else {
                          return Caml_array.caml_array_set(results, i, Pervasives.$at(prev, /* :: */[
                                          coin,
                                          /* [] */0
                                        ]));
                        }
                      } else {
                        return /* () */0;
                      }
                    });
                }
              } else {
                return (function (param) {
                    return Caml_array.caml_array_set(results, 0, /* [] */0);
                  });
              }
            }
            }(coin)), results);
        _param = param[1];
        continue ;
      } else {
        return results;
      }
    };
  };
  var match = value < 0;
  if (match) {
    return ;
  } else {
    return Caml_array.caml_array_get(make(Caml_array.caml_make_vect(value + 1 | 0, undefined), change), value);
  }
}

exports.min = min;
exports.makeChange = makeChange;
/* No side effect */
