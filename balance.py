def balance(arr):
	sum = 0
	for i in arr:
		sum += i

	left = 0
	i = 0
	while i < len(arr) - 1:
		if left < sum / 2:
			left += arr[i]
		i += 1

	if left == sum / 2:
		return True
	else:
		return False

print balance([1,2,3,4,10])
print balance([1,2,3,5])
print balance([1,2,3,4,4,6])
# print balance([10, 10])

