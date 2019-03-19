def solution(A):
	for i in range(0, len(A)-1):
		for j in range(len(A)-1, i, -1):
			if A[j] < A[j-1]:
				A[j-1], A[j] = A[j], A[j-1]


	check1 = A[len(A)-1] * A[len(A)-2] * A[len(A)-3]
	check2 = A[len(A)-1] * A[0] * A[1]

	print(A)

	if check1 > check2:
	 	return check1
	else:
	 	return check2

