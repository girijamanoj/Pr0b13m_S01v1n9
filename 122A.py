s=[4,7,47,74,477]
n=int(input())
if any(n%i==0 for i in s):
	print("YES")
else:
	print("NO")
