import functions as f
def rc(code):
    for line in code:
        if line[0] == "print":
            for word in line[1:]:
                print word

        else:
            print line[0], "is not recognized as a function"
