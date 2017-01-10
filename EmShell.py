greeting = open('greeting.txt', 'r')
print greeting.read()
greeting.close()

about_file = open('about.txt', 'r')
about = about_file.read()

errors = []
inputs = []
def get_input():
    Input = raw_input('>>>')
    inputs.append(Input)
    return Input.split(' ')

'''
functions is used in the if-elif-else to determine which command is used
run_code is used to run code from a .em
re (regex) is used to determine which parameters are strings
'''
import functions as f
from run_code import run_code
import re

no_params = ['about', 'commands_written', 'stats', 'errors']

number_vars = {}

while True:
    #Get input
    Input = get_input()
    
    #Test for empty input
    deleted = 0
    
    for index in range(len(Input)):
        if Input[index - deleted] == '':
            del Input[index - deleted]
    
    deleted = 0
    
    if Input == []:
        continue

    for item in range(len(Input) - 1):
		
        '''This iterates through all of the items in Input and replaces them with
        their numeric value'''
        
        if len(Input[item + 1]) == 0:
            if Input[item + 1][0] == '!': 
                if Input[item + 1][1:] in number_vars.keys():
                    Input[item + 1] = number_vars[Input[item + 1][1:]]

                else:
                    errors.append('NameError: ' + Input[item + 1][1:] + ' is undefined')
                    print 'NameError: ' + Input[item + 1][1:] + ' is undefined'
            
        float_compile = '^\d+\.\d+$'
        int_compile = '^\d+$'
        
        if type(Input[item + 1]) == str:
            if re.match(float_compile, Input[item + 1]):
                Input[item + 1] = Input[item + 1].split('.')
                
                #The following line of code converts [whole part, decimal part] into a flaot
                
                Input[item + 1] = int(Input[item + 1][0]) + int(Input[item + 1][1]) / 10 ** len(Input[item + 1][1])
                
            elif re.match(int_compile, Input[item + 1]):
                Input[item + 1] = int(Input[item + 1])
              
    if Input[0] == 'about':
        print about
  
    elif Input[0] == 'errors':
        for error in errors:
            print error
      
    elif Input[0] == 'commands_written':
        for item in inputs:
            print item
      
    elif Input[0] == 'stats':
        print 'Commands executed: ' + str(len(inputs))
        print 'Errors made:' + str(len(errors))
    
    elif Input[0] == 'add':
        print sum(Input[1:])
      
    elif Input[0] == 'subtract':
    	  print f.subtract(Input[1:])
    
    elif Input[0] == 'multiply':
	      print f.multiply(Input[1:])
    
    elif Input[0] == 'divide':
	      print f.divide(Input[1:])
    
    elif Input[0] == 'modulo':
	      print f.modulo(Input[1:])
	 
    elif Input[0] == 'power':
	      if len(Input) == 3:
	          print int(Input[1]) ** int(Input[2])
	      else:
	          errors.append('ArgumentError: power takes 2 arguments')
	          print 'ArgumentError:power takes 2 arguments'
    
    elif Input[0] == 'exit':
    	  break
      
    elif Input[0] == 'defint':
    	  number_vars[Input[1]] = int(Input[2])
    	
    elif Input[0] == 'run':
        code = open(Input[1])
        print code.read()
        print 'Why, that\'s some nice code you\'ve got there!\nDon\'t worry, you\'ll be able to run it soon!'
        code.close()

    elif Input[0] == 'print':
        for param in Input[1:]:
            print param
            
    else:
        print 'NameError: ' + Input[0] + ' is undefined.'
        errors.append('NameError: ' + Input[0] + ' is undefined.')
  
    if len(errors) == 0 or errors[-1] != 'NameError: ' + Input[0] + ' is undefined.':
        if len(Input[1:]) == 0 and Input[0] in no_params:
            print 'ArgumentError: Please include at least one argument.'
            errors.append('ArgumentError: Please include at least one argument.')
            
about_file.close()
