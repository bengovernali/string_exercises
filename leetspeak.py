def leetspeak(paragraph):
    new_paragraph = ""
    for letter in paragraph:
        if letter == "a": 
            new_paragraph += "4"
        elif letter == "A":
            new_paragraph += "4"
        elif letter == "e":
            new_paragraph += "3"
        elif letter == "E":
            new_paragraph += "3"
        elif letter == "g":
            new_paragraph += "6"
        elif letter == "G":
            new_paragraph += "6"
        elif letter == "i":
            new_paragraph += "1"
        elif letter == "I":
            new_paragraph += "1"
        elif letter == "o":
            new_paragraph += "0"
        elif letter == "O":
            new_paragraph += "0"
        elif letter == "s":
            new_paragraph += "5"
        elif letter == "S":
            new_paragraph += "5"
        elif letter == "t":
            new_paragraph += "7"
        elif letter == "T":
            new_paragraph += "7"
        else:
            new_paragraph += letter
    
    return new_paragraph


print(leetspeak("There once was an ugly barnacle. He was so ugly, everybody died. The end!"))