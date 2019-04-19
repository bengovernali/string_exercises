def uppercase_a_string(given_string):
    new_string = ""
    index = 0
    for letter in given_string:
        if index == 0:
            new_string += letter.upper()
        else:
            new_string += letter
        index += 1
    return new_string

print(uppercase_a_string("bobby"))