nums = [12,4,56,4,13,764,3,76]

def selection_sort(nums):
    for i in range(len(nums)):
        minVal = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minVal]:
                minVal=j
        if minVal!=i:
            nums[i],nums[minVal]=nums[minVal],nums[i]
    return nums

print(selection_sort(nums))