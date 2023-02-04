def my_function(**product_properties):
    print("____________________________________________")
    for k in product_properties:
        print("product " + k + ": " + product_properties[k])
    print("____________________________________________")

my_function(price = "12.5%", duration="12 m.",name = "DEPOSIT 12")
my_function(name = "DEPOSIT 3",price = "11.5%", duration="3 m.", currency = "KZT")