def reverse_a_string(given_string):
    new_string = ""
    index = len(given_string) - 1
    while index >= 0:
        new_string += given_string[index]
        index -= 1
    return new_string

print(reverse_a_string("battleground"))