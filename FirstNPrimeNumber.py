def isPrimeNumber(m):
    count = 0
    for i in range(2,m):
        if(m%i==0):
            count+=1

    if(count==0):
        return True
    else:
        return False


def PrimeNumbersList(n):
    primeNumbersList = []
    for i in range(1, n+1):
        if(isPrimeNumber(i)):
            primeNumbersList.append(i)

    return primeNumbersList

n = 100
print("first ",n," prime numebrs: ",PrimeNumbersList(n))
