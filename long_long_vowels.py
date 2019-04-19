def long_long_vowels(given_string):
    result = ""
    index = 0
    while index < len(given_string):
        if given_string[index] in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            if given_string[index] == given_string[index - 1]:
                result += given_string[index] * 4
            else:
                result += given_string[index]
        else:
            result += given_string[index]
        index += 1
    return result

print(long_long_vowels("Spoon"))
