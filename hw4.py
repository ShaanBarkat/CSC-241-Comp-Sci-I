#hw4
#Shaan Barkat Collab with Anthony Marsilio

def partition(lst,letter):
    x = letter.upper()
    for i in lst:
            if i.upper() >= x:
               print(i)#Finally!!

def points(x1,y1,x2,y2):
    distance = (((x2-x1)**2+(y2-y1)**2)**(1/2))
    if x2-x1==0 or y2-y1==0:
        print ('The slope is infinity and the distance is', distance)
    else:
        slope = ((y2-y1)/(x2-x1))
        print ('The slope is', slope, 'and the distance is', distance)
    
def numVowels(c):
    file = open(c)
    read1 = file.read()
    file.close
    read = read1.lower()
    count = 0
    vowels = ('aeiou')
    for letter in read:
        if letter in vowels:
            count+=1
    return count

def numLen(s, target):
    listlength = s.split()
    lator = 0
    for wordlength in listlength:
        wordlength1 = len(wordlength)
        if wordlength1 == target:
            lator += 1
    return lator

if __name__=='__main__':
         import doctest
         print( doctest.testfile('hw4TEST.py'))

        
    
    
