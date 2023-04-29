x = "awesome"

def myfunc():
    global x
    x = "good"
    print("Python is " + x)

def myfunc2():
    print("Python is " + x)

myfunc()
myfunc2()