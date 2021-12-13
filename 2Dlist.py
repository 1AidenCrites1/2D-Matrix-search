matrix = [[1, 4,], [22, 6, 98], [12, 3, 62], [1293, 322, 100]]
target = int(input("Choose a target number: "))

import bisect
lst = []

#converts nested list into a list so it can be searched
for elem in matrix:
    lst.extend(elem)

matrix = lst

#searches through matrix using bisect
bisect.bisect(matrix, target)

#checks to see if target is in matrix
found = target in matrix
print(found)

#99.24% faster than all python3 submissions on leetcode
