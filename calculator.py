#!/usr/local/bin/python2.7
import array
import re
import string
import pdb

######
#TODO:
#   enable without whitespace in input string



###########################################################
# UNIT TESTS

#Run unit tests
def Run_All_Tests():
    Test_add()
    Test_subtract()
    Test_add_subtract()
    Test_multiply()
    Test_divide()
    Test_multiply_divide()
    Test_exponent()
    Test_combos()
    Test_misc()

def Test_add():
    parsed = parse('4 + 56')
    template = ['4','56', '+']
    assert(parsed == template)
    
    parsed = parse('4 + 56 + 6 + 40')
    template = ['4','56','+','6','+','40','+']
    assert(parsed == template)

def Test_subtract():
    parsed = parse('4 - 56')
    template = ['4','56','-']
    assert(parsed == template)
    
    parsed = parse('4 - 56 - 6 - 40')
    template = ['4','56','-','6','-','40','-']
    assert(parsed == template)

def Test_add_subtract():
    parsed = parse('4 + 5 - 6')
    template = ['4','5','+','6','-']
    assert(parsed == template)

    parsed = parse('4 + ( 5 - 6 )')
    template = ['4','5','6','-','+']
    assert(parsed == template)

def Test_multiply():
    parsed = parse(' 4 * 87 ')
    template = ['4','87','*']
    assert(parsed == template)

    parsed = parse('3 * 90 * 4')
    template = ['3','90','*','4','*']
    assert(parsed == template)

def Test_divide():
    parsed = parse(' 4 / 87 ')
    template = ['4','87','/']
    assert(parsed == template)

    parsed = parse('3 / 90 / 4')
    template = ['3','90','/','4','/']
    assert(parsed == template)

def Test_multiply_divide():
    parsed = parse('4 * 5 / 56')
    template = ['4','5','*','56','/']
    assert(parsed == template)

    parsed = parse('4 * ( 5 / 32 )')
    template = ['4','5','32','/','*']
    assert(parsed == template)

    parsed = parse('1 * 434345 / 78953 * 21145 / 85241')
    template = ['1','434345','*','78953','/','21145','*','85241','/']
    assert(parsed == template)

def Test_exponent():
    parsed = parse(' 3 ^ 4 ')
    template = ['3','4','^']
    assert(parsed == template)

    parsed = parse(' 3 ^ 4 ^ 5')
    template = ['3','4','5','^','^']
    assert(parsed == template)

    parsed = parse(' 3 ^ ( 4 ^ 5 ) ^ 6')
    template = ['3','4','5','^','6','^','^']
    assert(parsed == template)

def Test_combos():
    parsed = parse('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3')
    template = ['3','4','2','*','1','5','-','2','3','^','^','/','+']
    assert(parsed == template)

def Test_misc():
    parsed = parse('( ( 4 + 5 ) * 6 )')
    template = ['4','5','+','6','*']
    assert(parsed == template)

    parsed = parse('')
    template = []
    assert(parsed == template)



###########################################################

opers = {
    '+':    (2,'L'),
    '-':    (2,'L'),
    '*':    (3,'L'),
    '/':    (3,'L'),
    '^':    (4,'R'),
}


#This function sets up the input string by recognizing whether a
# character is an operator or a number
def setup_input(inp = None):
    if inp is None:
        inp = raw_input('expression: ')

    #remove whitespace and create tokens
    tokens = inp.strip().split()
    tokenized = []

    for token in tokens:
        if token in opers:
            tokenized.append(('OPER', (token, opers[token][0], opers[token][1])))
        elif token == '(' or token == ')':
            tokenized.append(('PAREN',token))
        elif (token.isdigit() == True):
            tokenized.append(('NUM', token))
        else:
            return 0
    return tokenized



#This function will parse the input using the Shunting-yard algorithm
# and yield a string to be interpreted using Reverse Polish notation 
def shunting_yard(tokens):
    outputQ = []
    operstack = []

    for token, val in tokens:
        """print '\n'
        print "outputQ: "
        print outputQ
        print "operstack: " 
        print operstack"""

        #if we have a number
        if token is 'NUM':
            outputQ.append(val)
        #if we have an operator
        elif token is 'OPER':
            t1, prec1, asso1 = val
            while operstack and operstack[-1][0] is 'OPER':               
                t2, prec2, asso2 = operstack[-1][1]
                if (asso1 == 'L' and prec1 == prec2) or (prec1 < prec2):
                    outputQ.append(operstack.pop()[1][0])
                else:
                    break
            operstack.append((token,val))
        elif val == '(':
            operstack.append((token,val))
        elif val == ')':
            try:
                while operstack[-1][0] is not 'PAREN':
                    outputQ.append(operstack.pop()[1][0])
            except KeyError:
                return -1
            operstack.pop()
            
    while operstack:
        t2, val = operstack.pop()
        if t2 is 'PAREN':
            return -1
        outputQ.append(val[0])
    return outputQ


def parse(rawstring):

    tokenized = setup_input(rawstring)
    if tokenized == 0:
        print "Invalid input"
        return False
    formatted = shunting_yard(tokenized)
    return formatted


#Main
def main():
    print "#########################################################"
    print "First we run unit tests"
    print "..."
    Run_All_Tests()
    print "Done with unit tests"
    print "#########################################################"


    #create game board
    print "\nWelcome to the Calculator"

    while True:
        #Capture user input string
        rawstring = raw_input("Enter your calculation: ")
        print("Your input was: " + rawstring)

        formatted = parse(rawstring)
        if formatted == -1:
            print "Error! You had unmatched parenthesis. Try again"
        else:
            print formatted

    print "\n"


main()
