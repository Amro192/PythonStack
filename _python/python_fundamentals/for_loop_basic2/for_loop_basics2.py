#-1
def noPositive(ar):
    for x in range(len(ar)):
        if ar[x]>=0:
            ar[x]="big"
    print(ar)
noPositive([1,4,-1,-2])            

#-2
def numPositives(ar):
    counter=0
    for i in range(len(ar)):
        if ar[i]>0:
            counter+=1
    ar[-1]=counter
    return ar
print(numPositives([3,4,5,6,-1,-2,4]))

#-3
def sumTotal(ar):
    sumtotals=0
    for i in range(len(ar)):
        sumtotals+=ar[i]
    return sumtotals
print(sumTotal([1,5,3,7,-2]))    

#-4
def avgTotal(ar):
    sumtotals=0
    avgtotals=0
    for i in range(len(ar)):
        sumtotals+=ar[i]
    avgtotals=sumtotals/len(ar)
    return avgtotals
print(avgTotal([1,5,3,7,-2]))  

#-5
def lest(ar):
    length=0
    length=len(ar)
    return length
print(lest([]))    

#-6
def minN(ar):
    if len(ar)==0:
        return False
    
    else:
        min=ar[0]
        for i in range(len(ar)):
            if min > ar[i]:
                min = ar[i]
        return min
print(minN([1,2]))  

#-7
def maxN(ar):
    if len(ar)==0:
        return False
    
    else:
        max=ar[0]
        for i in range(len(ar)):
            if max < ar[i]:
                max = ar[i]
        return max
print(maxN([]))  

#-8
def analys(ar):
    sum = sumTotal(ar)
    avg = avgTotal(ar)
    min =minN(ar)
    max = maxN(ar)
    length = lest(ar)
    analysis = { 
        'sumTotal:': sum,
        'avarage:' : avg,
        'minimum:' : min,
        'maximum:' : max,
        'length:'  :length
    }
    return analysis
print(analys([5,4,3,22]))

#-9
import math
def reverse(ar):
    x=0
    i=0
    
    while i <=len(ar)/2 and x >= len(ar)/2 *-1: 
        ar[i] , ar[x-1] = ar[x-1] , ar[i]
        x-=1
        i+=1
    return ar
print(reverse([1,2,3,4,5,6,7,8,9,10]))
ar =[::-1]



