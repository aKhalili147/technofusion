"""
    DESCRIPTION:

        Write a program to find the sum of the first 1000 prime numbers (простые числа).

"""

def check(n):
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

sum = 0
for i in range(2,1001) :
	check_prime = check(i)
	if (check_prime) :
		sum += i

print("Sum of prime numbers in interval 2 and 1001:"+str(sum))

