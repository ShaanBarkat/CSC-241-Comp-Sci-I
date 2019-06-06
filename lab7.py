#lab 7
#Shaan Barkat Collab with Anthony Marsilio

def reverse(diction):
    d = {}
    for swap in diction:
        d[diction[swap]] = swap
    return d
        
def letter2number(grade):
    a = grade.lower()
    diction = {'a':4.0, 'b':3.0, 'c':2.0, 'd':1.0, 'f':0}
    b =a[0]
    if b not in diction:
        return 'unknown grade'
    if '+' in a:
        diction[b] += 0.3
    if '-' in a:
        diction[b] += -0.3
    if a == 'a+':
        return 'unknown grade'
    if a == 'f-':
        return 'unknown grade'

    return diction[b]


def names():
    counts = {}
    name ='xxx'
    while True:
        name = input('Enter next name: ').upper()
        if name == '':
            break
        elif name in counts:
            counts[name]+=1
        else:
            counts[name]=1
    keys = list(counts.keys())
    keys.sort()
    for name in keys:
        print("There are {} students named {}".format(counts[name], name))


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab7TEST.py') )
    
        
    
    
    
        
    
    
    
