def choose(n,k): 
	""" finding n choose k, returns numerical value for 
	number of ways to chooose k elements out of n """ 

	#base cases
	if n == k: 
		return 1
	if k == 1: 
		return n
	if k > n: 
		return 0

	#equation 
	n_minus_1_choose_k = choose(n-1,k)
	n_minus_1_choose_k_minus_1 = choose(n-1,k-1)
	result = n_minus_1_choose_k + n_minus_1_choose_k_minus_1

	return result

choose(6,2)