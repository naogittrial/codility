def solution(N, A):
	resultarray = [0] * N
	maxnum = 0
	for i in range(0, len(A)):
		if A[i] <= N:
			resultarray[A[i]-1] += 1

		else:
			#最大値を取得
			for j in range(0, len(resultarray)):
				if resultarray[j] > maxnum:
					maxnum = resultarray[j]
			resultarray = [maxnum] * N

	return resultarray




			