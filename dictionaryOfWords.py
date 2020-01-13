"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""


word_definitions["damsel"] = "a young unmarried woman"
word_definitions["svelte"] = "slender and elegant"
word_definitions["bifurcation"] = "the division of something into two branches or parts"


"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["damsel"])
print(word_definitions["svelte"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
