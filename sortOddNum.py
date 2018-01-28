def sort_array(arr):
    # Return a sorted array.
    if len(arr) == 0:
        return arr
    for i, v in enumerate(arr):
        min = arr[i]
        minIndex = i
        print i , '-->' ,v
        for j,k in enumerate(arr[i+1:]):
            if min > arr[j]:
                min = arr[j]
                minIndex = j
        tmp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = tmp
        print arr   
    print arr
sort_array([5, 3, 2, 8, 1, 4])
