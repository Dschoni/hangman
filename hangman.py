# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:26:18 2016

@author: gu32hej
"""

import random
words = ['haus','baum','auto','baustelle']
word = words[random.randint(0,len(words)-1)]
Leben = 6
solution = []
for i in word:
    solution.append('.')
print ''.join(solution)
while ''.join(solution) != word:
    if Leben == 0:
        print 'Sorry, verloren. Das Wort war: '+word
        break
    letter = raw_input('Buchstabe eingeben: ')
    if len(letter)!=1:
        print 'Bitte nur einen Buchstaben eingeben'
        continue
    else:
        found = False
        for i in range(len(word)):
            if letter == word[i]:
                found = True
                solution[i]=letter
        if found:
            print solution
            continue
        else:
            print 'Leider falsch!'
            Leben-=1
            print 'Du hast noch %s Leben.'%Leben
print 'Prima! Gewonnen!'

    