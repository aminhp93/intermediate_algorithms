def reverse(arr):
	i = 0
	while i < len(arr)/2:
		temp = arr[i]
		arr[i] = arr[len(arr) - i - 1]
		arr[len(arr) - 1- i] = temp
		i += 1
	return arr

print reverse([1,3,2,4,5,7]) == [7,5,4,2,3,1]
