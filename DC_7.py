n = int(input())
p = {}
for i in range(n):
	k = input()
	if k in p :
		print(k+str(p[k]))
		p[k]+=1
	else:
		print('OK')
		p[k] = 1
