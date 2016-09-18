import random

def ten_by_ten():
	arr = []
	i = 0
	while i < 10:
		arr.append([])
		j = 0
		while j < 10:
			if random.randint(0,1) == 0:
				arr[i].append('D')
			else: 
				arr[i].append('E')
			j += 1
		i += 1

	print arr
ten_by_ten()
