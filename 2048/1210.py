#!/usr/local/bin/python3

arr1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
arr2 = [list(row) for row in zip(*arr1)]
print(arr2)

arr3 = [row[::-1] for row in arr1]
print(arr3)