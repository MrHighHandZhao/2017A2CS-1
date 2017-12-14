"""
Harry Xue
"""
def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    return bunnyEars(bunnies-1)+2

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonacci(x-2)+fibonacci(x-1)

def bunnyEars2(bunnies):
    if bunnies == 0:
        return 0
    elif bunnies%2 == 0:
        return bunnyEars2(bunnies-1)+3
    elif bunnies%2 == 1:
        return bunnyEars2(bunnies-1)+2

def triangle(x):
    if x == 0:
        return 0
    return triangle(x-1)+x

def sumDigits(x):
    if x == 0:
        return 0
    return sumDigits(int(x/10))+x%10

def count7(x):
    if x == 0:
        return 0
    elif x%10 == 7:
        return count7(int(x/10))+1
    elif x%10 != 7:
        return count7(int(x/10))

def count8(x):
    if x == 0:
        return 0
    elif x%10 == 8 and (int(x/10))%10 != 8:
        return count8(int(x/10))+1
    elif x%10 == 8 and (int(x/10))%10 == 8:
        return count8(int(x/10))+2
    elif x%10 != 8:
        return count8(int(x/10))

def powerN(x1,x2):
    if x2 == 1:
        return x1
    return x1*powerN(x1,x2-1)

def countX(x):
    if x == '':
        return 0
    elif x[-1:] == 'x':
        return countX(x[:-1])+1
    elif x[-1:] != 'x':
        return countX(x[:-1])

def countHi(x):
    if x == '':
        return 0
    elif x[-2:] == 'hi':
        return countHi(x[:-2])+1
    else:
        return countHi(x[:-1])

def changeXY(x):
    if x == '':
        return ''
    elif x[-1:] == 'x':
        return changeXY(x[:-1])+'y'
    else:
        return changeXY(x[:-1])+x[-1:]

def changePi(x):
    if x == '':
        return ''
    elif x[-2:] == 'pi':
        return changePi(x[:-2])+'3.14'
    else:
        return changePi(x[:-1])+x[-1:]

def noX(x):
    if x == '':
        return ''
    elif x[-1:] == 'x':
        return noX(x[:-1])
    else:
        return noX(x[:-1])+x[-1:]

def array6(x,i):
    if i == len(x):
        return False
    elif x[i] == 6:
        return True
    return array6(x, i+1)

def array11(x,i):
    if i == len(x):
        return 0
    elif x[i] == 11:
        return array11(x,i+1)+1
    return array11(x,i+1)

def array220(x,i):
    if i == len(x)-1:
        return False
    elif x[i]*10 == x[i+1]:
        return True
    return array220(x,i+1)

def allStar(x):
    if x[:-1] == '':
        return x[-1:]
    else:
        return allStar(x[:-1])+'*'+x[-1:]

def pairStar(x):
    if x == '':
        return ''
    elif x[-1:] == x[-2:-1]:
        return pairStar(x[:-1])+'*'+x[-1:]
    else:
        return pairStar(x[:-1])+x[-1:]

def endX(x):
    if x == '':
        return ''
    elif x[-1:] == 'x':
        return endX(x[:-1])+'x'
    else:
        return endX(x[:-1])+x[-1:]

def countPairs(x):
    if x == '':
        return 0
    elif x[-1:] == x[-3:-2]:
        return countPairs(x[:-1])+1
    else:
        return countPairs(x[:-1])

def countAbc(x):
    if x == '':
        return 0
    elif x[0] == 'a' and x[1] == 'b' and x[2] == 'a':
        return countAbc(x[1:])+1
    elif x[0] == 'a' and x[1] == 'b' and x[2] == 'c':
        return countAbc(x[1:])+1
    else:
        return countAbc(x[1:])

def count11(x):
    if x == '':
        return 0
    elif x[0] == '1' and x[1] == '1':
        return count11(x[2:])+1
    else:
        return count11(x[1:])

def stringClean(x):
    if x == '':
        return ''
    elif x[-1] == x[-2:-1]:
        return stringClean(x[:-1])
    else:
        return stringClean(x[:-1])+x[-1:]

def countHi2(x):
    if len(x) < 2:
        return 0
    elif x == '':
        return 0
    elif x[0] != 'x' and x[1] == 'h' and x[2] == 'i':
        return 1 + countHi2(x[1:])
    else:
        return countHi2(x[1:])

def parenBit(x):
    if x[0] != '(':
        if x[len(x)-1] != ')':
            return parenBit(x[1:-1])
        return parenBit(x[1:])
    elif x[len(x)-1] != ')':
        return parenBit(x[:len(x)-1])
    else:
        return x

def nestParen(x):
    if x == '':
        return True
    elif (x[0] == '(') and (x[len(x)-1] == ')'):
        return nestParen(x[1:len(x)-1])
    else:
        return False

def strCount(m,n):
    if m == '':
        return 0
    elif m[0:len(n)] == n:
        return strCount(m[len(n):],n)+1
    else:
        return strCount(m[1:],n)

def strDist(m,n):
    if m == 0:
        return 0
    elif m[0:len(n)] != n:
        return strDist(m[1:],n)
    elif m[-len(n):] != n:
        return strDist(m[:-1],n)
    return len(m)m[:0],n,i-1)
print(strCopies('iiiiij','iii',3))
