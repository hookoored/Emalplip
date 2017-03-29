import functions as f
def rc(code):
    for line in code:
        split_line = line.split(' ')
        if split_line[0] == "print":
            for word in split_line[1:]:
                print word

        else:
            print split_line[0], "is not recognized as a function"
