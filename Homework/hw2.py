# hw2.py - Shaan Barkat
# Collab with Anthony Marsilio
def returnThree(z):
    if z[2:]:
        return (z[:3])   
    else:
        print ("''")

def returnN(x,y):
    if y>(len(x)):
        print ("''")
    else:
        return (x[:y])

def firstChars(z): 
    if z == []:
        print('The list provided as a parameter was empty.')
    for char in z:
        if char > (char[:1]):
            print (char[:1])

def printGreater(x,y):
    for h in x:
        if h>y:
            print (h, end = ' ')
    
           
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw2TEST.py') )

    
    

    
