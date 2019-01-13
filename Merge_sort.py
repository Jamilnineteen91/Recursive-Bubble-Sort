nums = [1,4,5,576,12,83,3,24,46,100,2,4,1]

def Merge_sort(nums):
    if len(nums)<=1:
        return nums

    first=0
    last=len(nums)-1
    middle=(first+last)//2
    left=nums[:middle]
    right=nums[middle:]
    left=Merge_sort(left)
    right=Merge_sort(right)
    return merge(left,right)


def merge(group_a,group_b):
    sorted_list=[]
    index_a=0
    index_b=0
    length_a=len(group_a)
    length_b=len(group_b)
    while index_a < length_a or index_b < length_b:
        if index_a < length_a and index_b < length_b:
            if group_a[index_a]<=group_b[index_b]:
                sorted_list.append(group_a[index_b])
                index_a+=1
            else:
                sorted_list.append(group_b[index_b])
                index_b+=1
        elif index_a < length_a:
            sorted_list.append(group_a[index_a])
            i+=1
        else:
            sorted_list.append(group_b[index_b])
    return sorted_list

def merge_sort(nums):
    divide(nums,0,len(nums)-1)

def divide(nums,first,last):
    if first<last:
        middle=(first+last)//2
        divide(nums,first,middle)
        divide(nums,middle+1,last)
        return merger(nums,first,middle,last)

def merger(nums,first,middle,last):
    sorted_list=[]
    group_a=nums[first:middle+1]
    group_b=nums[middle+1:last]
    a_index=0
    b_index=0
    for k in range(first,last+1):
        if group_a[a_index]<=group_b[b_index]:
            sorted_list[k]=group_a[a_index]
            a_index+=1
        else:
            sorted_list[k]=group_b[b_index]
    return sorted_list

print(Merge_sort(nums))