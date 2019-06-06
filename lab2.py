##### Lab 2 #####
# Collabed with Anthony Marcilio
# Section 1
def initials():
   x = input('Please enter your first name: ')
   y = input('Please enter your last name: ')
   print(x,y,'your initials are',x[0]+y[0])

# Section 2
def corv():
    x = input('Please enter a lower case letter: ')
    if x in 'aeiou':
        print (x,'is a vowel')
    else:
        print(x,'is a consonant')

# Section 3
def pigLatin():
    print('English to Pig Latin Translator')
    x = input('Please enter a lower case English word: ')
    if x[0] in 'aeiou':
        print(x, 'translates to', x+('ay'))
    else:
        print(x,'translates to',x[1:]+x[0]+('ay'))
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab2TEST.py') )
