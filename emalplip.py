from sys import argv
from run_code import rc
from shell import shell

if len(argv) == 1:
    shell()

else:
    code_file = open(argv[1])
    code = code_file.read()
    rc(code.split('\n'))
