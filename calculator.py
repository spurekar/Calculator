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
    """Test_add()
    Test_subtract()
    Test_add_subtract()"""

def Test_add():
    parsed = parse('4 + 56')
    template = ['4','56', '+']
    assert(parsed == template)
    
    parsed = parse('4+56+6+40')
    template = ['4','+',['56','+',['6','+','40']]]
    assert(parsed == template)

def Test_subtract():
    parsed = parse('4-56')
    template = ['4','-','56']
    assert(parsed == template)
    
    parsed = parse('4-56-6-40')
    template = ['4','-',['56','-',['6','-','40']]]
    assert(parsed == template)

def Test_add_subtract():
    parsed = parse('4+5-6')
    template = ['4','+',['5','-','6']]
    assert(parsed == template)


###########################################################

opers = {
    '+':    2,
    '-':    2,
    '*':    3,
    '/':    3,
    '^':    4,
    '(':    9,
    ')':    0
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
            tokenized.append((token,opers[token]))
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
        print "outputQ: "
        print outputQ
        print "operstack: " 
        print operstack
        pdb.set_trace()

        #if we have a number
        if token is 'NUM':
            outputQ.append(val)
        #if we have an operator
        elif token in opers:
            t1, prec1 = token,val
            while operstack:
                t2, prec2 = operstack[-1]
                if ( token != '^' and prec1 <= prec2) or (token == '^' and prec1 < prec2):
                        if t1 != ')':
                            if t1 != '(':
                                operstack.pop()
                                outputQ.append(t2)
                            else:
                                break
                        else:
                            if t2 != '(':
                                operstack.pop()
                                outputQ.append(t2)
                            else:
                                operstack.pop()
                                break
                else:
                    break
            if t1 != ')':
                operstack.append((token,val))
    while operstack:
        t2, prec2 = operstack[-1]
        operstack.pop()
        outputQ.append(t2)
    return outputQ


def parse(rawstring):

    tokenized = setup_input(rawstring)
    if tokenized == 0:
        print "Invalid input"
        return False
    print tokenized
    formatted = shunting_yard(tokenized)
    return formatted


formatted = parse('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3')
print formatted


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
        #rawstring = raw_input("Enter your calculation: ")
        rawstring = get_input()
        print(rawstring)


        formatted = parse(rawstring)
        print formatted

        """
        #Go through each index in the list and perform operations as necessary
        for i,char in enumerate(string):
            if (char == '+'):
                if (string[i-1].isdigit and string[i+1]):
        """

    print "\n"
