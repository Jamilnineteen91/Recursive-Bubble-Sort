nums = [1,4,5,-12,576,12,83,-5,3,24,46,100,2,4,1]

def Merge_sort(nums):
    if len(nums)<=1:
        return nums

    middle=int(len(nums)//2)#int is used to handle a floating point result.
    left=Merge_sort(nums[:middle])#Divises indices into singular lists.
    print(left)#Prints list division, lists with singular items are the final results.

    right=Merge_sort(nums[middle:])#Divises indices into singular lists.
    print(right)#Prints list division, lists with singular items are the final results.

    return merge(left,right)


def merge(left, right):
    sorted_list=[]
    index_L=0 #index_L is used to incrementally ascend the left list.
    index_R=0 #index_R is used to incrementally ascend the right list.

    #Lists containing more than one item will enter the while loop where they'll be sorted.
    while index_L < len(left) and index_R < len(right):
            #Prints left & right groups that are have entered the while loop.
            print(left[index_L:], right[index_R:])

            if left[index_L]<=right[index_R]:
                sorted_list.append(left[index_L])
                index_L+=1

 #Prints the current sorted_list state, the smallest item between the left group and right group has been inserted into sorted_list.
                print(sorted_list)
            else:
                sorted_list.append(right[index_R])
                index_R+=1

 #Prints the current sorted_list state, the smallest item between the left group and right group has been inserted into sorted_list.
                print(sorted_list)

    #Lists containing one item will be added to the sorted_list.
    #The append function is unable to append lists into new_list, hence why'+=' is used.
    #Unable to use 'index_L' as a list index since the incrementation only takes place in the while loop,hence why 'index_L:' and 'index_R:' are used.
    sorted_list+= left[index_L:]
    sorted_list+= right[index_R:]
    return sorted_list


print(Merge_sort(nums))
