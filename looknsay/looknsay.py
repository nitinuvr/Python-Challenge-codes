import numpy as np

def  looknsay(N):
	i, j, k =0, 1, 0
	looksay=[]
	
	if N=='1':
		return 1
	elif N=='2':
		return 11
	else:
		while i<len(N):
			k=N[i]
			i+=1
			if str[i]==str[i-1]:
				j+=1
			else:
				looksay.append(j)
				looksay.append(k)
				j=1

print("Insert Term Number Here: ")

			