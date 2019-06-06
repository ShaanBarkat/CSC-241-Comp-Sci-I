# hw3
# Shaan Barkat
# Collab with Anthony Marsilio
def printMultiples(n, m):
    c = m + 1
    for ans in range(c):
        if ans > 0:
            print (ans*n, end=' ')

def customSpam(Name, Amount, Email):
    z = Amount.upper()
    x = list(z)
    q = Name.title()
    a = ('''Dear {},
We would like to let you know about a great opportunity.
You can make {} dollars in just a few short weeks!
This is a limited-time offer.
Please contact us at {} for more information.''').format(q,' '.join(x), Email)
    print (a)

def ion2e(word):
        if word[-3:] == 'ion':
            return (word[:-3]+'e')
        else:
            return (word)

def startsWith(letter, lst):
    a = letter.lower()
    lengthofletter = len(letter)
    for letterlist1 in lst:
        b = letterlist1.lower()
        if b[:lengthofletter] == a:
            print (letterlist1)

if __name__=='__main__':
         import doctest
         print( doctest.testfile('hw3TEST.py'))

    
    
