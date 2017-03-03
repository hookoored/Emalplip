import sys
import run_code

if len(sys.argv) == 1:
    execfile("EmShell.py")
else:
    code_file = open(sys.argv[1])
    run_code.rc(code_file.read())
    code_file.close()
