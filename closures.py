def outer(state):
    element=state
    print("element in outer",element)
    def inner(data):
        inside=data
        print("element in inner",element)
        print("element in inner",inside)
    inner("first call")

    return inner

ref=outer("Strong")
ref("India")
ref("Japan")