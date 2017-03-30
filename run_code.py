import functions as f
import re

def rc(code):
    empty = re.compile("^$")
    only_spaces = re.compile("^\s+$")
    for line in code:
        split_line = line.split(' ')
        if empty.match(line) or only_spaces.match(line):
            continue
            
        elif split_line[0] == "print":
            for word in split_line[1:]:
                print word
                
        else:
            print split_line[0], "is not recognized as a function"
