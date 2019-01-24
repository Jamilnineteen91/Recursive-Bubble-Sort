nums = [12,4,56,4,13,764,3,76]


def Insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i-1,-1,-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
            else:
                break

    return nums

print(Insertion_sort(nums))


