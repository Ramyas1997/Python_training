def willCallYouBack(cb):
print("started working")
cb("India")
print("Still in fun")
cb("America")
print("and still in fun")
cb("Russia")
print("and and still in fun")
cb("Mangolia")
print("Wrapped it")

def processIt(data):
print("Received", data)

willCallYouBack(processIt)