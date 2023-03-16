def inserction_sort(array):

    for index in range(0, len(array)):
        current_element = array[index]

        print(index,"     ", array)

        while index > 0 and array[index-1] > current_element:
            array[index] = array[index-1]
            index -= 1
            
        array[index] = current_element

array = [81,15,4,20,7,47,14,20,4]
inserction_sort(array)
print("sorted:", array)