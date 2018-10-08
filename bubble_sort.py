
def bubble_sort(alist):
    for i in range(0,len(alist)-1,1):
        for j in range(0,len(alist)-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist

myList=[4,54,12,65,8,43,3,956]
print(bubble_sort(myList))

def rec_bubble_sort(alist):
    for i in range(len(alist)-1):#Iterates through the list
        if alist[i]>alist[i+1]:
            alist[i],alist[i+1]=alist[i+1],alist[i]#change of the state of the list occurs here
            rec_bubble_sort(alist) #Recursive call takes place here
        else: #Base case is alist[i],alist[i+1]
            pass
    return alist
rec_list=[4,54,12,65,8,43,3,956]
print(rec_bubble_sort(rec_list))

#Compare the duration of each bubble sort

#bubble sort time
print(timeit.timeit("""def bubble_sort(alist):
    for i in range(0,len(alist)-1,1):
        for j in range(0,len(alist)-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist

myList=[4,54,12,65,8,43,3,956]""""",number=5))

#recursive bubble sort time
print(timeit.timeit("""def rec_bubble_sort(alist):
    for i in range(len(alist)-1):#Iterates through the list
        if alist[i]>alist[i+1]:
            alist[i],alist[i+1]=alist[i+1],alist[i]#change of the state of the list occurs here
            rec_bubble_sort(alist) #Recursive call takes place here
        else: #Base case is alist[i],alist[i+1]
            pass
    return alist
rec_list=[4,54,12,65,8,43,3,956]""""",number=5))
