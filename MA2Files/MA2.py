"""
Solutions to module 2 - A calculator
Student: Albin Svensson
Mail: albin.svensson.7131@student.uu.se
Reviewed by:
Reviewed date:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper
import time #markera
import random #markera



class SyntaxError(Exception): #Syntaxerrors in the input expression
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception): #Errors in the evaluation of the expression div
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def statement(wtok, variables): #The main function that calls the other functions
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    while wtok.get_current() == ',': #handels multiple assignments #markera
        wtok.next()
        result = assignment(wtok, variables)
    if wtok.is_at_end():
        return result
    else:
        raise SyntaxError("Expected EOL")

def assignment(wtok, variables): #assigning values to variables
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            var_name = wtok.get_current()
            wtok.next()
            variables[var_name] = result
        else:
            raise SyntaxError("Expected name after '='")
    return result

def expression(wtok, variables): #Handles addition and subtraction from term
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result
    
def term(wtok, variables): #Handles multiplication and division from factor
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ('*', '/', '%', '**','//'): #Modulus and exponential and // operator added
        operator = wtok.get_current()
        wtok.next()
        if operator == '*':
            result *= factor(wtok, variables)
        elif operator == '/':
            divisor = factor(wtok, variables)
            if divisor == 0:
                raise EvaluationError("Division by zero!")
            result /= divisor
        elif operator == '%':   #Modulus operator #markera
            result %= factor(wtok, variables)
        elif operator == '//': #markera 
            divisor = factor(wtok, variables)
            if divisor == 0:
                raise EvaluationError("Division by zero!")
            result = float(result // divisor)

        elif operator == '**':  # Exponentiation operator
            exponent = factor(wtok, variables)
            if result == 0 and exponent != 0:
                raise EvaluationError("0 cannot be raised to a non-zero power")
            if result < 0 and not exponent.is_integer():
                raise EvaluationError("Negative base with non-integer exponent")
            result **= exponent
        
        
    return result

def factor(wtok, variables): #Handles parentheses, numbers, functions and variables
    """ See syntax chart for factor"""
    FUNCTIONS_1 = {'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': math.log,
    'fac': math.factorial, 'abs': abs, 'sqrt': math.sqrt, 'tan': math.tan}
    FUNCTIONS_N = {'sum': sum, 'max': max, 'min': min, 'avg': lambda x: sum(x)/len(x)} #Functions with multiple arguments
    FUNCTIONS_0 = {'random': random.random, 'time': time.ctime} #Functions with no arguments, time and random, markera
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == "|": #Handles absolute value
        wtok.next()
        result = abs(expression(wtok, variables))
        if wtok.get_current() != "|":
            raise SyntaxError("Expected '|'")
        wtok.next()

    # Checking for negative numbers
    elif wtok.get_current() == "-":
        wtok.next()
        result = -factor(wtok, variables)

    # Checking for valid function names or variables
    elif wtok.is_name() and wtok.get_current().isalpha():
        func_name = wtok.get_current()
        wtok.next()

        # Handle log and fac directly within factor
        if func_name == "log":
            if wtok.get_current() != "(":
                raise SyntaxError("Expected '(' after 'log'")
            wtok.next()
            arg = assignment(wtok, variables)
            if arg <= 0:
                raise EvaluationError(f"Logarithm of negative number {arg} was attempted")
            result = math.log(arg)
            if wtok.get_current() != ")":
                raise SyntaxError("Expected ')'")
            wtok.next()

        
        elif func_name == "fac":
            if wtok.get_current() != "(":
                raise SyntaxError("Expected '(' after 'fac'")
            wtok.next()
            arg = assignment(wtok, variables)
            if arg < 0:
                raise EvaluationError(f"Factorial of negative number {arg} was attempted")
            elif arg % 1 != 0:
                raise EvaluationError(f"Factorial of non-integer number {arg} was attempted")
            result = math.factorial(int(arg))
            if wtok.get_current() != ")":
                raise SyntaxError("Expected ')'")
            wtok.next()
        



        # Handle other FUNCTIONS_1 and FUNCTION_N
        elif func_name in FUNCTIONS_1.keys():
            if wtok.get_current() != "(":
                raise SyntaxError("Expected '('")
            else:
                result = FUNCTIONS_1[func_name](arglist(wtok, variables)[0])

        elif func_name in FUNCTIONS_N.keys():
            result = FUNCTIONS_N[func_name](arglist(wtok, variables))

        elif func_name in FUNCTIONS_0.keys(): #Function that handels functions with no arguments, time and random markera
            result = FUNCTIONS_0[func_name]()   

        elif func_name in variables.keys():
            result = variables[func_name]

        elif func_name == "vars":
            result = "printing variables"
        else:
            raise EvaluationError(f"Unknown function '{func_name}'")
    else:
        raise SyntaxError("Expected number/name or '('")
    
    return result

def arglist(wtok, variables): #creates a list of arguments for functions
    result = []
    if wtok.get_current() == '(':
        wtok.next()
        result.append(assignment(wtok, variables))
        while wtok.get_current() == ',':
            wtok.next()
            result.append(assignment(wtok, variables))
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
    else:
        raise SyntaxError("Expected '('")

    return result
 
def main():
    """Handles: the iteration over input lines, commands like 'quit' and 'vars' and raised exceptions.
    Starts with reading the init file"""
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = '/Users/albinsvensson/Desktop/Python/Programmeringsteknik2/MA2Files/MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            #print('init  :', line)
        else:
            #raise SyntaxError('No more lines in init file')
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        
        if wtok.get_current() == 'vars':
            for var, value in variables.items():
                print(f'{var} has the value: {value}')

        if wtok.get_current() == 'clear': #Clears the variables markera
            variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
            print('Variables cleared')

        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except TokenError as te:
                print('*** Syntax error: Incorrect parentheses', te)
                print(f"Error occurred at token '{wtok.get_current()}' after '{wtok.get_previous()}'")

            except EvaluationError as ee:
                print('*** Evaluation error:', ee)
                print(f"Error occurred at token '{wtok.get_current()}' after '{wtok.get_previous()}'")
            
            except SyntaxError as se:
                print('***Syntax error:', se)
                print(f"Error occurred at token '{wtok.get_current()}' after '{wtok.get_previous()}'")
                

if __name__ == "__main__":
    main()