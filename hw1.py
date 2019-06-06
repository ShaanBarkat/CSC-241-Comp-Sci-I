# hw1.py - Shaan Barkat
# Collabed with Anthony Marcilio
# IDLE Exercises
'''
>>> s1 = '&'
>>> s2 = '#'
>>> s1*2+s2
'&&#'
>>> s2*2+s1
'##&'
>>> ((s1*2+s2)*2)
'&&#&&#'
>>> s1*10
'&&&&&&&&&&'
>>> ((s1*2+s2*2)*3)
'&&##&&##&&##'
>>> ((s1*5+s2*5)*3)
'&&&&&#####&&&&&#####&&&&&#####'
'''
def total():
    z = eval(input('Enter a price: '))
    x = eval(input('Enter a quantity: '))
    if z>0 and x>0:
        print('The total price is: $',z*x)
    elif z<=0 or x<=0:
        print('Error: both numbers must be greater than zero.')

def posNegZero():
    z = eval (input('Enter a number: '))
    if z<0:
        print ('You entered a negative number.')
    if z>0:
        print ('You entered a positive number.')
    if z==0:
        print ('You entered zero.')

def square():
    z = int (input('Enter an integer: '))
    x = z**(1/2)
    if z==0:
        print (z, 'is 0 squared.')
    elif z%x>0:
        print (z,'is not a perfect square.')
    else:
        print (z, 'is',int(z**(1/2)),'squared.')

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw1TEST.py') )

        


        
        
