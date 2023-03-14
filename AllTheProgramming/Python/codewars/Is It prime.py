num = int(input())
isPrime = True
for i in range(2,num//2):
    if num % i == 0:
        isPrime = False
        break
        
if isPrime == True:
    print(str(num) + " is Prime")
else:
    print(str(num) + " is NOT Prime")
