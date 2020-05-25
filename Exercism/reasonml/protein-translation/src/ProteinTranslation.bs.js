// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var $$String = require("bs-platform/lib/js/string.js");
var Caml_js_exceptions = require("bs-platform/lib/js/caml_js_exceptions.js");
var Caml_builtin_exceptions = require("bs-platform/lib/js/caml_builtin_exceptions.js");

function codonToProtein(param) {
  switch (param) {
    case "AUG" :
        return "Methionine";
    case "UAC" :
    case "UAU" :
        return "Tyrosine";
    case "UCA" :
    case "UCC" :
    case "UCG" :
    case "UCU" :
        return "Serine";
    case "UGG" :
        return "Tryptophan";
    case "UGC" :
    case "UGU" :
        return "Cysteine";
    case "UUA" :
    case "UUG" :
        return "Leucine";
    case "UUC" :
    case "UUU" :
        return "Phenylalanine";
    default:
      return "STOP";
  }
}

function proteins(rna) {
  var protein;
  try {
    protein = codonToProtein($$String.sub(rna, 0, 3));
  }
  catch (raw_exn){
    var exn = Caml_js_exceptions.internalToOCamlException(raw_exn);
    if (exn[0] === Caml_builtin_exceptions.invalid_argument) {
      return /* [] */0;
    } else {
      throw exn;
    }
  }
  if (protein === "STOP") {
    return /* [] */0;
  } else {
    return /* :: */[
            protein,
            proteins($$String.sub(rna, 3, rna.length - 3 | 0))
          ];
  }
}

exports.proteins = proteins;
/* No side effect */