#!/usr/local/bin/python2.7
import array
import re
import string
import pdb


###########################################################
# UNIT TESTS

#Run unit tests
def Run_All_Tests():
    Test_add()
    Test_subtract()
    Test_add_subtract()

def Test_add():
    parsed = parse('4+56')
    template = ['4','+','56']
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

def parse(string):
    
    # Handle addition / subtraction
    for i,char in enumerate(string):
        if char == '+' or char == '-':
            #pdb.set_trace()
            lt = string[:i]
            rt = string[(i+1):]
            if (lt.isdigit() != True):
                lt=parse(lt)
            #pdb.set_trace()
            if (rt.isdigit() != True):
                rt=parse(rt)
            break
    return [lt, char, rt]


#Main

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
    """for i in string:
        pass
        if i.isalpha()
            print "Invalid input"
            break"""
    #rawstring = rawstring.upper()
    print(rawstring)

    #Replace each '(' with '[' and ')' with ']'
    """
    #Parse input string and save as a list
    string = re.split('([+-])',rawstring)
    print string
    """
    smita = parse(rawstring)
    print smita


    """
    #Go through each index in the list and perform operations as necessary
    for i,char in enumerate(string):
        if (char == '+'):
            if (string[i-1].isdigit and string[i+1]):
    """

print "\n"
