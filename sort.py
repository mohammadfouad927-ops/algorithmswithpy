def selection_sort(arr):
    for i in range(0,len(arr)-1):
        smallest= i
        for j in range(i+1,len(arr)):
            if (arr[smallest] > arr[j]):
                smallest = j
        
        # Swapping
        s = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = s
    
    return arr

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if(arr[j]>arr[j+1]):
                s = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = s
    return arr


print("SORTING WITH SELECTION SORT")
arr = [7,2,5,4,1,6,0,3]
print('The array before Sorting:')
for i in range(0,len(arr)):
    if i != len(arr)-1:
        print(i,end=',')
    else:
        print(i)
print('The array after sorting')
print(selection_sort(arr))
print("----------------------------------------")

#-----------------------------------------------------------

print("SORTING WITH BUBBLE SORT")
arr = [7,2,5,4,1,6,0,3]
print('The array before Sorting:')
for i in range(0,len(arr)):
    if i != len(arr)-1:
        print(i,end=',')
    else:
        print(i)
print('The array after sorting')
print(bubble_sort(arr))