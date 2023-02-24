def selection_sort(array):

    for index in range (0, len(array)):
        min_index = index

 """       print(index, "    ", array)"""

        for right in range (index + 1, len(array)):
            if  array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]


array = [15,11,16,18,23,5,10,22,21,12]
selection_sort(array)
print("sorted", array)