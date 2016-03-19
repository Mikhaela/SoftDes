def levenshtein(a,b): 
	""" returns Levenshtein distance between a and b 
		this function works, but is incredibly computationally demanding
		not a deep function, but it requires exponetially large depth as the 
		length of the strings increase
	"""

	if a == "": 
		return len(b)
	if b == "": 
		return len(a)

	#Strategy 1: change the first char to match
	if a[0] == b[0]: # if the first two characters are equal 
		option_1 = levenshtein(a[1:], b[1:]) # the cost will be the cost of rest of the trasformation 
	else: #if the first two characters are different
		option_1 = 1 + levenshtein(a[1:], b[1:]) #the cost will be 1+ the cost of the rest of the trasformation

	#Strategy 2: Drop first char of b 
	option_2 = 1 + levenshtein(a, b[1:])

	#Strategy 3: Drop firt char of a 
	option_3 = 1 + levenshtein(a[1:], b)

	return min(option_1, option_2, option_3)

	if __name__ == "__main__"
		import doctest 
		doctest

		#min() is a build in function 


