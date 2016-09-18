def sum_odd_fibonacci(num):
	i = 0 
	j = 1
	sum = 0
	s = []
	while j < num:
		next = i + j
		i = j
		j = next
		if i % 2 == 1:
			sum += i
	return sum

print sum_odd_fibonacci(4000000)

