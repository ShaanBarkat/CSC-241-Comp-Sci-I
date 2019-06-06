# lab9
# Shaan Barkat Collab with Anthony Marsilio
#1
def stackHeight(num):
    rows = 0
    while num>rows:
        rows += 1
        num -= rows
    return rows

#2
import random
def rollDice(n):
    lst = []
    for x in range(n):
        lst.append(random.randrange(1,7))
    return lst
        
#3   
def result(offense, defense):
    offense.sort()
    offense.reverse()
    defense.sort()
    defense.reverse()
    oLost, dLost = 0, 0
    for i in range(len(defense)):
        if offense[i] > defense[i]:
            dLost -= 1
        else:
            oLost -= 1
    return(oLost, dLost)

#4
def attack(n, oDice, dDice):
    d = {}
    for i in range(n):
        oRolls = rollDice(oDice)
        dRolls = rollDice(dDice)
        t = result(oRolls, dRolls)
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    return d

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab9TEST.py') )

    
