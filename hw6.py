# hw6
# Shaan Barkat Collab with Anthony Marsilio

import random
def game(num):
    correct = 0
    count = 0
    while (count<num):
        num1 = random.choice(range(0, 10))
        num2 = random.choice(range(0, 10))
        total = num1 + num2
        print(str(num1),'+',str(num2) + ' = ?')

        answer = eval(input('Enter answer: '))
        if total == answer:
            print('Correct')
            correct +=1
            count +=1
        else:
            print('Incorrect')
            count +=1
    print('You got',correct,'correct answers out of', str(num)+'.')

def craps():
    num1 = random.choice(range(1,7))
    num2 = random.choice(range(1,7))
    print(num1,num2)
    total = num1 + num2
    if total == 7 or total == 11:
        return 1
    elif total == 2 or total == 3 or total == 12:
        return 0
    else:
        total2 = 0
        while total2 != total or total2 != 7:
            num1 = random.choice(range(1,7))
            num2 = random.choice(range(1,7))
            print (num1,num2)
            total2 = num1+num2
            if total2 == total:
                return 1
            if total2 == 7:
                return 0

def quietCraps():
    num1 = random.choice(range(1,7))
    num2 = random.choice(range(1,7))
    #print(num1,num2)
    total = num1 + num2
    if total == 7 or total == 11:
        return 1
    elif total == 2 or total == 3 or total == 12:
        return 0
    else:
        total2 = 0
        while total2 != total or total2 != 7:
            num1 = random.choice(range(1,7))
            num2 = random.choice(range(1,7))
            #print (num1,num2)
            total2 = num1+num2
            if total2 == total:
                return 1
            if total2 == 7:
                return 0

def testCraps(a):
    c = 0
    for i in range(a):
        c+= quietCraps()
    i = c/a
    return i
    

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw6TEST.py') )

        
        
        
    
    
