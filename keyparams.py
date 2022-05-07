def keyparams(*normal,**params):
    print("normal parameters",normal)
    for x in params.keys():
        print("Key-->",x)
        print("Value is ",params[x])

keyparams(23,535,23,sno=1,name="Arjun",city="Mumbai")