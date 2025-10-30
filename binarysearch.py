
def binary_recursion_search(item,arr):
    if len(arr) > 0:
        right = len(arr)-1
        left = 0
        mid = (right + left) //2
        if(arr[mid] == item):
            print('Found')
            return 0
        elif (arr[mid] < item):
            left = mid +1
            binary_recursion_search(item,arr[left:])
        elif(arr[mid] > item):
            right = mid - 1
            binary_recursion_search(item,arr[:right+1])
    else:
        print("Not Found")
        return 1    

arr = [1,2,3,4,5,29,40,48,199,499,3299]
item = int(input('search about value: '))

binary_recursion_search(item,arr)

def binary_loop_search(item,arr):
    mid = 0
    left=0
    right = len(arr)-1
    while(right >= left):
        mid = (left + right) //2
        if arr[mid] == item :
            print("Found")
            return 0
        elif (arr[mid] < item):
            left = mid + 1 
        elif (arr[mid] > item):
            right = mid -1
    print("notFound")
    return 1

arr = [1,2,3,4,5,29,40,48,199,499,3299]
item = int(input('search about value: '))
binary_loop_search(item,arr)