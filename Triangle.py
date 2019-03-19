import itertools

def solution(A):
	count = 0
	if len(A) < 3:
		return 0

	possible = list(itertools.combinations(A,3))
	possible = list(set(possible))

	for i in range(len(possible)):
		check = possible[i]
		if check[0] + check[1] > check[2] and check[1] + check[2] > check[0] and check[2] + check[0] >check[1]:
			return 1
			break
			
	else:
	    return 0