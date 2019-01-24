nums = [34,-5,7,42,6,82,311,4,-45,7,33,12,74,3]



def Shell_sort(alist):
    sublistCount=len(alist)//2

    while sublistCount>0:
        for startPosition in range(sublistCount):
            gap_insertion_sort(alist,startPosition,sublistCount)

        print("Increment size:", sublistCount, "List:", alist)
        sublistCount=sublistCount//2

    return alist


def gap_insertion_sort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        for j in range(i-1,-1,-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
            else:
                break


print(Shell_sort(nums))



