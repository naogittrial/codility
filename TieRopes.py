def solution(K, A):
	count = 0
	length = 0
	for a in A:
		length += a
		if length >= K:
			count += 1
			length = 0
	return count
