a=30

def process(data):
    #a=20
    global a
    a+=data
    print("now a is ",a)

print("outside ",a)
process(89)
print("outside ",a)