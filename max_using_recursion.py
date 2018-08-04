def max(n):
	l = len(n)
	maximum = n[0]
	for i in range(1,l):
		if n[i] > maximum:
			maximum = n[i]
	return maximum

def recursive_max(n, l):
	if l == 1:
		return n[0]
	else :
		return maximum(n[l-1],recursive_max(n,l-1))
def maximum(a,b):
	if a > b:
		return a
	elif b > a:
		return b

l = [3,1,89,34]
x = recursive_max(l,4)
print(x)
