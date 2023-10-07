## --------------------------------------------------------------------- miss underestanding
## miss underestanding: estabah dar mohasebe 5 soale akhar (1d wasting time)
## # 30
## num1 = int(input())//10%10
#
## num2 = int(input())//10%10
#
## if num1+num2>5:
#
##     print('bale')

## # 31
## num1 = int(input())%10
#
## num2 = int(input())%10
#
## if num1%num2==0:
#
##     print('bale')

## # 32
## num1 = int(input())
#
## num2 = int(input())
#
## N1Hund = num1//100%10
#
## N2Tens = num2//10%10
#
## if N1Hund%N2Tens !=0:
#
##     print('bale')
#
## if num1%10 %2==0:
#
##     print('bale')

## # 33
## a = int(input())
#
## b = int(input())
#
## c = int(input())                               nkml
#
## if a 

## # 46
## for i in range(0,101,2):
##     print(i)

## # 47
## n = int(input('enter a number: '))
## for i in range(n-1,0,-1):
##         print(i)

## # 48
## n = int(input('enter a number: '))
## for i in range(1,n+1):
##     if n%i==0:
##         print(i)

## # 49
## n = int(input('enter a number: '))
## for i in range(1,n+1):
##     if n%i==0 and i%2!=0:
##         print(i)

## # 50
## import sympy
## inputt = int(input())
## if sympy.isprime(inputt)==True:
##     print(inputt,'is prime')
## else:
##     print(inputt,'is! prime')
# -------------------------------------------------------- miss underestanding



# 36
li =[]
for i in range(3):
    li.append(input())
print(max(li))

# 37
input1 = int(input())
input2 = int(input())
input3 = int(input())
li = [input1, input2, input3]
print(' '.join(map(str,(sorted(li))))) 


# 38
inpt = int(input('Enter 1-30 : '))
if inpt in (1,2,3,4,5,6,7):
    print('week 1')
elif inpt in (8,9,10,11,12,13,14):
    print('week 2')
elif inpt in (15,16,17,18,19,20,21):
    print('week 3')
elif inpt in (22,23,24,25,26,27,28,29,30):
    print('week 4')

# 39
fr_b_b = input('JUST binary or wont work: ')
if len(fr_b_b) == 4:
    fr_b_b = fr_b_b.replace('0','')
    print(fr_b_b)                                       
else:
    print('just binary white 4bite or wont work!'.upper())

# 40
n1_b_b = input('JUST binary or wont work: ')
n2_b_b = input('JUST binary or wont work: ')
if len(n1_b_b) == 3 and len(n2_b_b) == 3:
    i1 = int(n1_b_b,2)
    i2 = int(n2_b_b,2)
    fin = i1 + i2
    print(bin(fin)[2:])
else:
    print('just binary white 3bite or wont work!'.upper())

# 66
# nth == enomi
nterms = 500
n1,n2 = 0,1
count = 0
li = []
c = 0
while count < nterms:
    li.append(n1)
    nth = n1 + n2             
    n1 = n2
    n2 = nth
    count += 1
for i in range(100):
    inp = int(input())
    if inp in li and inp %2 !=0:
        # print(inp,'is in fibunacci')
        c  += 1
print(c)

# 67
nterms = 50
n1,n2 =1,1 
count = 0
li = []
c = 0
while count <= nterms:
    li.append(n1)
    nth = n1 + n2             
    n1 = n2
    n2 = nth
    count += 1
inp = int(input())
for w in li:
    if inp % w == 0:
        c  += 1
print(c)

# 68
inp = input()
s = 0
for i in inp:
    if i == '0': 
        s+=1
print(s)       

# 69
input1 = input()
input1 = input1.replace('0','')
print(input1)

# 70
for num in range(56,1985):
    li = []
    for i in range(1,1985):
        if num % i == 0:
            li.append(i)
    # print(f'{num} : {','.join(map(str,li))}')
    print(num,':',','.join(map(str,li)))

# 86
li =[]
n = int(input())
for i in range(n):
    inpt = li.append(int(input()))
print(max(li))

# 87 
li=[]
n = int(input())
for i in range(n):
    li.append(int(input()))
print(','.join(map(str,sorted(li,reverse=True))))

# 88
n = int(input())
li=[]
for i in range(n):
    li.append(int(input()))
li_srtd = li
li_srtd = sorted(li_srtd)
if li_srtd == li  :
    print('sorted')
elif li_srtd != li:
    print('   !sorted')

# 89
import sympy
li=[]
for i in range(10):
    i = 1
    inpt = int(input())
    if sympy.isprime(inpt)==False:
        li.append(inpt)
print(' , '.join(map(str,li)))

 # 90
from sympy import factorial
inp = []
inputL = []
inputOrig = []
n = int(input())
for i in range(n):
    inp.append(input())
    inputt = inp[i]
    inputL.append(factorial(inputt))
for w in range(n):
    print(inp[w],':',inputL[w])
    
# 106
c = 0
inpu = []
def odd(inpu,c):
    for w in inpu:
        if w % 2 == 0:
            c+=1                                      
    return c
for i in range(5):
    inpu.append(int(input()))
print(odd(inpu,c))

# 107
avrg = 0
inpu = []
def avout(inp,avrg,inpu):
    for w in inpu:
        if w-3 == avrg or w+3 == avrg:
            return w
for f in range(5):    
    inp= int(input())
    avrg+=inp
    inpu.append(inp)
avrg = avrg/5
print(avout(inp,avrg,inpu))

# 108
import sympy
# inp=[]
n = int(input())
def primecnt():
    c = 0
    for i in range(n):
        inp = int(input())
        if sympy.isprime(inp)==True:                      
            c += 1
    return c
print(primecnt())

# 109
import math
li = []
n = int(input())
def factorial():
    for i in range(n):
        # inputi = int(input())
        li.append(math.factorial(int(input())))
        # print(math.factorial(inputi))
factorial()
print (' , '.join(map(str, li)))

# 110
n = int(input())
def sortfnc():
    li = []
    for i in range(n):
        li.append(input())
    li = sorted(li)
    return li
print(sortfnc())

# 117
inputt = input()
print(inputt.title())

# 118
input_number = []
inputt = input()
for i in inputt:
    if i.isdigit():
        input_number.append(i)
print(','.join(input_number))

# 119
inputt = input()
inputt =inputt.replace('a','')
print(inputt)

# 120
inputt = input()
inputt = inputt.replace(' ','')
print(inputt)

# 121
fi = []
n1,n2 = '1111111111111111' , '1111111111111111' 
for w in range(0,16): 
    fi.append(int(n1[w]) + int(n2[w]))
print(''.join(map(str,fi)))