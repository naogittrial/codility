def solution(A):
	count = 0
	for i in range(0, len(A)):
		if A[i] == 0:
			for j in range(i, len(A)):
				if A[j] == 1:
					count += 1

		if count > 1000000000:
			return -1
			break

	return count
