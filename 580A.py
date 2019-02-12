n = int(input())
s = [int(i) for i in input().split()]
max_len = 1
length = 1
for i in range(n - 1):
	if s[i] <= s[i + 1]:
		length += 1
		if length > max_len:
			max_len = length
	else:
		length = 1
print(max_len)
