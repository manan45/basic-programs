def fibo(n):
	if n <= 1:
		return (n,0)
	else :
		(a,b) = fibo(n-1)
		print(b)
		return (a+b,a)


x = fibo(5)
print(x)