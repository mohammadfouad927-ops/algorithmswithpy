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

def merge_sort(arr):  # [6,3,4,1,5,2,7,0]
    if len(arr) > 1:
        s = 0
        e = len(arr)-1
        mid = (s+e) //2

        larr = arr[s:mid+1]
        rarr = arr[mid+1:e+1]

        sortedlarr = merge_sort(larr)
        sortedrarr = merge_sort(rarr)

        return merge(sortedlarr,sortedrarr)
    else:
        return arr

def merge(leftarray,rightarray):
    # lpa is standfor left-pointer-array and rpa is standfor rigth-pointer-array
    lpa = rpa = 0  
    sortedarr =[]
    while len(leftarray) != lpa or len(rightarray) != rpa:
        if len(leftarray) == lpa:
            sortedarr.append(rightarray[rpa])
            rpa += 1
        elif len(rightarray) == rpa:
            sortedarr.append(leftarray[lpa])
            lpa += 1
        elif leftarray[lpa] < rightarray[rpa]:
            sortedarr.append(leftarray[lpa])
            lpa += 1
        elif rightarray[rpa] < leftarray[lpa]:
            sortedarr.append(rightarray[rpa])
            rpa += 1
    return sortedarr
    

print("SORTING WITH SELECTION SORT")
arr = [7,2,5,4,1,6,0,3]
print('The array before Sorting:')
for i in range(0,len(arr)):
    if i != len(arr)-1:
        print(arr[i],end=', ')
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
        print(arr[i],end=', ')
    else:
        print(i)
print('The array after sorting')
print(bubble_sort(arr))
print("----------------------------------------")

#-----------------------------------------------------------

print("SORTING WITH MERGE SORT")
arr = [6,3,4,1,5,2,7,0]
print('The array before Sorting:')
for i in range(0,len(arr)):
    if i != len(arr)-1:
        print(arr[i],end=', ')
    else:
        print(i)
print('The array after sorting')
print(merge_sort(arr))
