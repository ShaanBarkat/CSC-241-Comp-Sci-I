# lab5
# Shaan Barkat

def hasOddWord(sent):
    w = sent.split()
    for i in w:
        if len(i)%2==1:
            return True
    return False

def dromes(filename):
    pols =''
    file=open(filename)
    words=file.read()
    file.close
    for char in'.,?':
        contents=contents.replace(char,'')
        words = words.upper
    lst = words.split()
    lines = file.readlines()
# Couldn't figure it out :/

def totalGreater(cutoff, lst):
    a = 0
    for num in lst:
        if num>cutoff:
            a+=num
    return a

def multiplesOf(m, lst):
    if m > 0:
        for i in range(len(lst)):
            if lst[i]%m==0:
                print (i,end=' ')
        else:
            return

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab5TEST.py') )

