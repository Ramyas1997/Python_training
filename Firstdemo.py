listx=[34,353,534,344,53,43,356,34,5344,6,34,53,5,35,34,534,534,3,34]

result = filter(lambda x:True if x%2==0 else False,listx)
print(list(result))

result1 = filter(lambda x:True if x>1000 else False,listx)
print(list(result1))