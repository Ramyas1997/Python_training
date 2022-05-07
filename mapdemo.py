listx=[34,353,534,344,53,43,356,34,534,6,34,53,5,35,34,534,534,3,34]

def examine(x):
    if(x%2==0):
        return "EVEN"
    else:
        return "ODD"

#map function takes each element from a collection
#  process it and yield a result for each element
# if there are n elements in the list the resultant array will also be of size name

result = map(examine,listx)
print(listx)
print(list(result))

result2 = map(lambda x:"Even" if x%2==0 else "ODD",listx)
print(list(result2))

result3 = map(lambda x:x*-1 if x%2==0 else x,listx)
print(list(result3))