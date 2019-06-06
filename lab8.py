#lab 8
#Shaan Barkat

        
def anagram(w1, w2):
    lst =[]
    for char in w1:
        lst.append(char)
    if len(lst)==len(w2):
        return True
    else:
        return False

'''
def findMinRow(lst):
    minIndex = 0
    lstSum = []
    if lst == []:
        return -1
    for i in range(len(lst)):
        minIndex.append(sum(lst[i]))
    for i in range(len(lstSum)):
        if i==0:
            ans = 0
        elif lstSum[i] < lstSum[ans]:
            ans = i
    return ans
'''

def findMinRow(lst):
    minIndex = 0
    lstSum = 0
    if len(lst)<1:
        return -1
    minSum = sum(lst[0])
    for i in range(len(lst)):
        lstSum = sum(lst[i])
        if lstSum < minSum:
            minSum = lstSum
            minIndex = i
    return minIndex
        

def mirror(word):
    d = {'t':'t','b':'d','d':'b','i':'i','o':'o','p':'q','q':'p','t':'t','u':'u','v':'v','w':'w','x':'x','l':'l','m':'m','n':'n'}
    res = ''
    for char in word:
        if char in d.keys():
            value = d.get(char)
            res += value
        else:
            return 'INVALID'
    return res[::-1]

import random

def numPicks():
    randInt = 0
    previous = []
    counter = 0
    while True:
        randInt = random.randrange(0,10)
        if randInt in previous:
            counter += 1
            break
        else:
            previous.append(randInt)
            counter += 1
    return counter

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab8TEST.py') )



            
            
