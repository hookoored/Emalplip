greeting = open('greeting.txt', 'r')
print greeting.read()
greeting.close()

about_file = open('about.txt', 'r')
about = about_file.read()

errors = []
inputs = []
def get_input():
    Input = raw_input('>>> ')
    inputs.append(Input)
    return Input.split(' ')

'''
functions is used in the if-elif-else to determine which command is used
run_code is used to run code from a .em
re (regex) is used to determine which parameters are strings
'''
import functions as f
from run_code import rc
import re

no_params = ['about', 'commands_written', 'stats', 'errors']

no_qoutes_needed = {
    'defint': 0,
    'run': 0
}

number_vars = {}

while True:
    #Get input
    Input = get_input()
    
    #Test for empty input
    deleted = 0
    
    for index in range(len(Input)):
        if Input[index - deleted] == '':
            del Input[index - deleted]
            deleted += 1
    
    deleted = 0
    
    if Input == []:
        continue
    
    #Name_error is used later
    name_error = False
    
    #quotes is used to reassemble strings that have been disassembled by split(" ").
    quotes = None
    
    #part_of_string stores the number of strings that have been combined.
    part_of_strings = 0

    for item in range(len(Input) - 1):
        index = item + 1 - part_of_strings
            
        if Input[index][0] in '\'"':
            quotes = Input[index][0]
            if Input[index][-1] == quotes and Input[index][-2] != '\\':
                Input[index] = [Input[index][1:-1]]
                
            else:
                Input[index] = [Input[index][1:]]
                    
        elif quotes != None:
            if Input[index][-1] == quotes and Input[index][-2] != '\\':
                Input[index - 1][0] += (' %s' % (Input[index][:-1]))
                quotes = None
                
            else:
                Input[index - 1][0] += (' %s' % (Input[index]))

            del Input[index]
            part_of_strings += 1
            index = item + 1 - part_of_strings
            
        '''This iterates through all of the items in Input and replaces them with
        their numeric value'''

        if quotes == None:
            if Input[index][0] == '!': 
                if Input[index][1:] in number_vars.keys():
                    Input[index] = number_vars[Input[index][1:]]

                else:
                    errors.append('NameError: \'' + Input[index][1:] + '\' is undefined')
                    print 'NameError: \'' + Input[index][1:] + '\' is undefined'
            
        float_compile = '^\d+\.\d+$'
        int_compile = '^\d+$'
        
        if type(Input[index]) == str:
            if re.match(float_compile, Input[index]):
                Input[index] = Input[index].split('.')
                #The following line of code converts [whole part, decimal part] into a flaot
                Input[index] = int(Input[index][0]) + int(Input[index][1]) / 10 ** len(Input[index][1])
                
            elif re.match(int_compile, Input[index]):
                Input[index] = int(Input[index])
                
            else:
                if no_qoutes_needed[Input[0]] == 0:
                    errors.append("NameError: '%s' is undefined." % (Input[index]))
                    print "NameError: '%s' is undefined." % (Input[index])
                    name_error = True
                
    if name_error == True:
        name_error == False
        continue
                              
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
        code = open(Input[1][0])
        rc(code.read().split(' '))
        code.close()

    elif Input[0] == 'print':
        for param in Input[1:]:
            print param[0]
            
    else:
        print 'NameError: \'' + Input[0] + '\' is undefined.'
        errors.append('NameError: ' + Input[0] + ' is undefined.')
  
    if len(errors) == 0 or errors[-1] != 'NameError: \'' + Input[0] + '\' is undefined.':
        if len(Input[1:]) == 0 and Input[0] in no_params:
            print 'ArgumentError: Please include at least one argument.'
            errors.append('ArgumentError: Please include at least one argument.')
            
about_file.close()
