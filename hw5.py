# hw5
# Shaan Barkat collab with Anthony Marsilio
def subStrings(z):
    lst = []
    for a in range(1,len(z)):
        if z[a] in z[a-1]:
            lst.append(z[a])
    return lst

def collatz(n):
    x = []
    x.append(n)
    while True:
        if n==1:
            return x
        elif n%2==0:
            n = (n//2)
            x.append(n)
        else:
            n = ((n*3)+1)
            x.append(n)
                            
def approxPi(error):
    denom = 1
    num = 4
    curr, prev = num/denom, 0
    while abs(curr-prev)>error:
        num*=-1
        denom+=2
        curr, prev = curr + num/denom, curr
    return curr
                            
def poly(lst, num):
    ans=0
    for i in range(len(lst)):
        ans = ans + lst[i]*num**i
    return ans


    return word
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py') )
    
                
        
            
                
        
        
        



    
    
