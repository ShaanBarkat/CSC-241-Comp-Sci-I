# lab3
# Shaan Barkat Collab with Anthony Marsilio

# Section 1
def print3Chars(z):
    for a in z:
        if len(a)> 3:
            print (a[0]+a[1]+a[2])
        else:
            print (a)
        
# Section 2
def avgLst():
   x = input('Please enter a list: ')
   if x == ('[]'):
        print ('n/a')
   else:
       return (sum(eval(x))/(len(eval(x))))

# Section 3
def magnitude(x):
    if x == []:
        print ("'n/a'")
    else:
        a = abs(max(x))
        b = abs(min(x))
        if a>b:
            return a
        if a<b:
            return b

# Section 4
def printevens(c):
    for a in c:
        if a%2==0:
            print (a)
    if len(c)==0:
        print ('Sorry, that list is empty.')

# Section 5
def printDivisors(q):
    for i in range(1,q+1):
        if q % i ==0:
            print(i)

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab3TEST.py') )


    


            
    
        


    
