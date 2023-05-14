from decimal import*
from fractions import Fraction
import time
getcontext().prec = 1000
n = int(input("Enter a number till which you need Prime numbers by moduli method \n:"))
i = 1
l = []
for i in range(9,n):#(2 is only even Prime number, 3 leads to infinite loop. Therefore I have not started from 3)#
    if i%2 !=0 and i % 5 != 0 and i % 3 != 0:
        l = l + [i]
#print(l)# List of Odd numbers out of divisibility by other than 2, 3, 5
begin = time.time()
nl = []
for j in l:
    i = 0
    for i in range(j):
        if 2 ** i < j < 2 ** (i + 1):
            break
    m = 2 ** (i - 1)
    #print("The numerator for n is = ",m)
    M = 2 ** (i + 1)
    Max = 2 ** (i + 2)
    lst = []

    #print(j)
    while M != m:
        M = M % j
        lst = lst + [M]
        M = M * 2
    lst = lst + [m]
    lst = lst + [m * 2]
    #print('List of remainders in the list for given odd number is', lst)
    rl = lst

    #print('Total number of moduli are', len(rl))
    ratio = (j - 1) / len(lst)
    #print("The ratio between (n-1) and Nom is   ", Fraction((j - 1), len(lst)))
    # returns Fraction
    # print((n-1)//len(lst),",", Fraction((n-1)%len(lst)),"/",len(lst))
    if (j - 1) % len(lst) == 0:
        nl = nl + [j]
print("list of Prime numbers out of Odd numbers is\n",nl)
print(len(nl))
end = time.time()
print("Time taken to calculate list of Prime numbers is", end - begin)
ls = []
a = 0
for num in range(9, n):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            a += 1
            ls = ls + [num]
            # print(a, '|',num )
# print(ls)
print(len(ls))

# using sieve method
# Uncommon elements in List
res_list = []
for i in nl:
    if i not in ls:
        res_list.append(i)
for i in ls:
    if i not in nl:
        res_list.append(i)

    # printing the uncommon
print("The uncommon of two lists is : " + str(res_list))
print(len(res_list))
