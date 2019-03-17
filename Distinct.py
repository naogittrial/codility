def solution(A):
	distinct = []
	for i in range(0,len(A)):
		if A[i] not in distinct:
			distinct.append(A[i])
	return len(distinct)