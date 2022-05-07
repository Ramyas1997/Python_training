def sum(*data):
    print(type(data),data)

    sum=0
    for x in data:
        sum+=x;

    return sum

print(sum(1,2))
print(sum(1,23,5))
print(sum(35,33,63,63))
print(sum(34,32,15,6,63))
print(sum(34,36,67,3,435,63)) 