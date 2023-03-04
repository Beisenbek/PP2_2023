f = open("demofile.txt","rb")

x = f.read()

for i in range(len(x)):
    print(x[i])
