nums = [12,4,56,4,13,764,3,76]

# O(n^2)
def Insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i-1,-1,-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
            else:
                break

    return nums

print(Insertion_sort(nums))

# Recursive Insertion Sort
#O(n)
def Rec_Insertion_Sort(nums):
    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            nums[i-1],nums[i]=nums[i],nums[i-1]
            Rec_Insertion_Sort(nums)
        else:
            pass
    return nums

print(Rec_Insertion_Sort(nums))
