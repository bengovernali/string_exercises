def uppercase_a_string(given_string):
    new_string = ""
    for letter in given_string:
        new_string += letter.upper()
    return new_string

print(uppercase_a_string("beeple"))