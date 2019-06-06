# Shaan Barkat
# Collab Anthony Marsilio
def lineLengths(file):
    filename = open(file,'r')
    contents = filename.readlines()
    filename.close
    x = 0
    for z in contents:
        x+=len(z)
        print (str(len(z)),end ="+")
    print("0="+str(x))

def monogram(n):
    monoAco=''
    lst = n.split()
    for splitname in lst:
        splitname2 = splitname[0].upper()
        monoAco+=splitname2
    return monoAco
    

def pay(rate,hours):
    if hours > 40 and hours < 60:
        overtimehours = hours - 40
        return ((rate*40)+(rate*overtimehours*1.5))
    elif hours >= 60:
        overtimehours2 = hours-60
        return ((rate*40)+(rate*20*1.5)+(rate*overtimehours2*2))
    else:
        return (hours*rate)

def average(fname):
    q = open(fname, 'r')
    w = q.read()
    q.close()
    WordSum=0
    if len(w)== 0:
        return 0.0
    wLst = w.split()
    for wword in wLst:
        WordSum+=(len(wword))
    return (WordSum/len(wLst))

if __name__=='__main__':
         import doctest
         print( doctest.testfile('lab4TEST.py'))

    
