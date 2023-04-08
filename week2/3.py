thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1965
}

thisdict["a"] = "b"
thisdict.update({"year2": "2000"})


for x, y in thisdict.items():
    print(x,y)

x = thisdict.values()

print(x)

if x > 10:
    print(x)
    x = 3
if x < 5:
    print("!",x)


if x > 10:
    print(x)
    x = 3
elif x < 5:
    print("!",x)