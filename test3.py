from functools import reduce
listx = [2,3,5,7,9,35,353,535,34,34,534,534]

def find_prime(num):
    if num>1:
        flag = True
        for i in range(2,num):
            if num%i==0:
                flag= False
                break
    
    return flag

prime_iterator=filter(find_prime,listx)

res = list(prime_iterator)
print(res)

print(reduce(lambda a,b:a if a>b else b,res))  