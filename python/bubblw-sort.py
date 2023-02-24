def bubble_sort(array):

    for final in range(len(array), 0, -1):
        for current in range(0, len(array) - 1):
            print("sorting: ",array)

            if array[current] > array[current + 1]:
                 array[current], array[current + 1] = array[current + 1], array[current]

array = [15,11,16,18,23,5,10,22,21,12]
bubble_sort(array)
print("sorted:  ", array)