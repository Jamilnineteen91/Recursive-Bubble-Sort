nums = [34,-5,7,42,6,82,311,4,-45,7,33,12,74,3]

def Shell_sort(alist):
    sublistCount=len(alist)//2

    while sublistCount>0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist,startPosition,sublistCount)

        sublistCount=sublistCount//2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        for j in range(i-1,-1,-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
            else:
                break

Shell_sort(nums)
print(nums)