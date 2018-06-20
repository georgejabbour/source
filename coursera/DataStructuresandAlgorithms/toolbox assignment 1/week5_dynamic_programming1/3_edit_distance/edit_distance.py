# Uses python3
def edit_distance(s, t):
	#lengths
	n=len(s)+1
	m=len(t)+1

	#initialize D
	D=[[0] * (m) for x in range(n)]
	D[0] = [x for x in range(m)]

	#fill matrix
	for j in range(1,m):
		for i in range(1,n):
			
			insert=D[i][j-1]+1
			delete=D[i-1][j]+1
			mismatch=D[i-1][j-1]+1

			match=D[i-1][j-1]

			if s[i-1]==t[j-1]:
				D[i][j]=match
			else:
				D[i][j]=min(insert,delete,mismatch)
	
	return D[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
