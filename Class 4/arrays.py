import array as ar
array_num = ar.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))
print("number of occurances of 3 in the array: "+str(array_num.count(3)))
array_num.reverse
print("Reversed array: "+str(array_num))