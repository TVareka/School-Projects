print("Please enter an amount in cents less than a dollar.")
cents = int(input())
print("Your change will be:")
print("Q:", cents//25)
cents_2 = cents%25
print("D:", cents_2//10)
cents_3 = cents_2%10
print("N:", cents_3//5)
cents_4 = cents_3%5
print("P:", cents_4//1)
