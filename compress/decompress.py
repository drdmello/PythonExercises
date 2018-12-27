#! /usr/bin/env python

import sys
import unittest

def decompress(inputString):
    '''
    Return an uncompressed version of the input string, expanding expressions of the form num[string] as (num * string)
    '''
    
    if __debug__:
        print '*** INFO: ' + 'decompress called with ' + inputString

    result = ''
    numberOfRepeatsString = ''
    numberOfRepeats = 0
    inRepeatExpression = False
    repeatExpression = ''
    inputStringIndex = 0
    
    while (inputStringIndex < len(inputString)):
        
        currentCharacter = inputString[inputStringIndex:inputStringIndex+1]
        if __debug__:
            print '*** INFO: ' + 'current-char: ' + currentCharacter + ' at position: ' + str(inputStringIndex)

        if currentCharacter.isalpha():
            if not inRepeatExpression:
                result += currentCharacter
            else:
                repeatExpression += currentCharacter
        elif currentCharacter.isdigit():
            numberOfRepeatsString += currentCharacter
        elif currentCharacter == '[':
            numberOfRepeats = int(numberOfRepeatsString)
            numberOfRepeatsString = ''
            inRepeatExpression = True
        elif currentCharacter == ']':
            if inRepeatExpression:
                result += numberOfRepeats * repeatExpression
                numberOfRepeats = 0
                repeatExpression = ''
                inRepeatExpression = False
        else:
            assert False, '*** ERROR: Unexpected character: %s' % currentCharacter

        if __debug__:
            print '*** INFO: ' + 'numOfRepeatsString: ' + numberOfRepeatsString + ' numOfRepeats: ' + str(numberOfRepeats)

        inputStringIndex += 1
           
    return result

## Unit-test code

class NoRepeats(unittest.TestCase):
    def test(self):
        self.assertEqual(decompress('abc'), 'abc')
        self.assertEqual(decompress(''), '')
        self.assertEqual(decompress('z'), 'z')

class SimpleRepeats(unittest.TestCase):
    def test(self):
        self.assertEqual(decompress('5[lulu]'), 5*'lulu')
        self.assertEqual(decompress('3[abc]4[ab]c'), 3*'abc' + 4*'ab' +'c')  # Example accompanying problem
        self.assertEqual(decompress('10[c]c'), 11*'c')
        
class NestedRepeats(unittest.TestCase):
    def test(self):
        self.assertEqual(decompress('2[3[a]b]'), 'aaabaaab')


if __name__ == '__main__':
    unittest.main()
