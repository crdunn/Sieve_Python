import time
while (True):
	try:
		x = input("See all prime numbers from 0 to a given number:")
		n = int(x)
		break
	except:
		print("Please enter an integer")

start = time.time()
arr = [False, False, True]
flip = True
for i in range(3,n):
	if(flip):
		arr.append(True)
	else:
		arr.append(False)
	flip = not flip

for i in range(2,n):
    if (arr[i]):
        j = 3*i
        while(j < n):
            arr[j]=False
            j+=2*i
end=time.time()
exTime = end-start
allPrimes = []
for i in range(n):
    if(arr[i]):
        allPrimes.append(i)
print(allPrimes)
print("Number of primes: ", len(allPrimes))
print("Execution time: ", exTime)