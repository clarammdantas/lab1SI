def max(array):
	max = array[0]
	for i in array:
		if i > max:
			max = i

	return max

def min(array):
	min = array[0]
	for i in array:
		if min > i:
			min = i

	return min