from functools import reduce

listx=[3435,34,36,34,34,534,34,534,34,23,23,534,35]

result = reduce(lambda x,y: x+y,listx)

print(result)

result = reduce(lambda x,y: x if x>y else y, listx)

print(result)

result = reduce(lambda x,y: x if x<y else y, listx)

print(result)
# a reduce function will take a callback function as parameters and
# the call back needs to have two parameters 
# reduce functionc calls the callback by passing the current element and previous result2
# each time except for the first time, first time it passes first and second elements 
# reduce will produce only result
# if list has n elements result will have only element