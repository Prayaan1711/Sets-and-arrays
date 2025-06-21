import array as arr

array_num = arr.array('i', [1,3,5,3,7,9,3])

print("orriginal: " + str(array_num))

print("No. of occurances of 3 in array: " + str(array_num.count(3)))

array_num.reverse()
print("Reverse order: ")
print(array_num)