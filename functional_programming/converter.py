from functools import partial


js_code = """
let myString = "Hello world!";
console.log(myString);
"""

def contains(character, string):
    return character in string

def index_of(character, string):
    return string.index(character)

semicolon = partial(contains, ";")
index_bracket_open = partial(index_of, "(")
index_bracket_close = partial(index_of, ")")

def pairs_of(characters, string):
    partial_index = partial(partial, index_of)
    partial_functions = map(partial_index, characters)



pairs_of("()", None)
