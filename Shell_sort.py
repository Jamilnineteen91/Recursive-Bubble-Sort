nums = [34,-5,7,42,6,82,311,4,-45,7,33,12,74,3]



def Shell_sort(alist):
    sublistCount=len(alist)//2

    while sublistCount>0:
        for startPosition in range(sublistCount):
            Rec_gapInsertionSort(alist,startPosition,sublistCount)

        print("Increment size:", sublistCount, "List:", alist)
        sublistCount=sublistCount//2

    return alist


def Rec_gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        if alist[i-1]>alist[i]:
            alist[i-1],alist[i]=alist[i],alist[i-1]
            Rec_gapInsertionSort(alist,start,gap)
        else:
            pass

print(Shell_sort(nums))



