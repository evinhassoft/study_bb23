def bubble_sort(array):

    for final in range(len(array), 0, -1):
        for current in range(0, len(array) - 1):

            if array[current] > array[current + 1]:
                print(array)
                array[current], array[current + 1] = array[current + 1], array[current]

array = [81,15,4,20,7,47,14,20,4]
bubble_sort(array)
print("sorted:  ", array)