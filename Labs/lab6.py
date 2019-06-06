#Lab 6
#Shaan Barkat Collab with Anthony Marsilio
# Problem 1
def doubles(lst):
    a = []
    for b in range(len(lst)):
        if len(lst) == 0:
            return []
        if b>0:
            if lst[b-1]*2 == lst[b]:
                a.append(lst[b])
    return a

# Problem 2        
def mod(n, k):
    while n>=k:
        n = n-k
    return n

# Problem 3
def coins(n):
    lst = []
    for amount in [25, 10,5, 1]:
        while n>=amount:
            lst.append(amount)
            n -= amount
    return lst

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab6TEST.py') )

