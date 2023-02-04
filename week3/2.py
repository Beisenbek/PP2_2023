def my_function(*kids):
    n = len(kids)
    x = 2
    if x < n:
        print("The youngest child is " + kids[x])

my_function("Emil", "Tobias", "Linus")