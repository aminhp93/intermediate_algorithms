def palindrome(str):
	i = 0 
	while i < len(str)/2:
		if str[i] != str[len(str) - i -1]:
			return False
		i += 1
	return True

print palindrome('abcba')

def largest_palindrome(str):
	i = 0 
	length = 0
	result = ""
	while i < len(str) - 1:
		j = len(str) - i - 2 
		while j > i:
			k = j + 1
			if str[i] == str[j] and palindrome(str[i:k]) == True:
				if len(str[i:k]) > length:
					length = len(str[i:k])
					result = str[i:k]
			j -= 1
		i += 1
	return result

print largest_palindrome('abcbabcdedcbabbcccdcda')


