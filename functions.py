'''
This is a custom module used to calculate what the user inputs
'''
def subtract (List):
    retval = List[0]
    for item in List[1:]:
        retval -= item
    return retval

def multiply (List):
    retval = 1
    for item in List:
        retval *= item
    return retval

def divide (List):
    retval = List[0]
    for item in List[1:]:
        retval = retval / item
    return retval

def modulo (Int):
    if len(Int) != 2:
        return 'ArgumentError: modulo only takes 2 arguments.'
        errors.append('ArgumentError: modulo only takes 2 arguments.')
    else:
        if Int[0] < Int[1]:
            errors.append('ArgumentError: The dividend is smaller than the divisor.')
            return 'ArgumentError: The dividend is smaller than the divisor.'
        else:
            return Int[0] % Int[1]
            
