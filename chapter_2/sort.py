
arr = [31, 41, 59, 26, 41, 58]
def sort(arr):
	toSort = arr
	for j in range(1, len(toSort)):
		key = toSort[j]
	 	i = j - 1
		while i >= 0 and toSort[i] > key:
	 		toSort[i+1] = toSort[i]
	 		i = i - 1
		toSort[i+1] = key
	return toSort	

print sort(arr)	