def longest_word(str):
	words = str.split()
	length = 0
	result = ""
	for i in words:
		if len(i) > length:
			length = len(i)
			result = i
	return result

print longest_word('amin a apple app')
