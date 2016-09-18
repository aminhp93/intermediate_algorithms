def three_and_five(min, max):
	result = 0
	i = min
	while i <= max:
		if (i % 3 == 0 or i % 5 == 0) and (i % 15 != 0):
			result += i
		i += 1
	return result
print three_and_five(10, 4000000)


