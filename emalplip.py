from sys import argv
from run_code import rc

if len(sys.argv) == 1:
    execfile("shell.py")

else:
    code_file = open(argv[1])
    code = code_file.read().split('\n').split(' ')
    rc(code)
