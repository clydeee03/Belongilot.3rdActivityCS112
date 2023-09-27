print("Sales Tax")
while True:
    sales = float(input("Enter sales here:"))
    result = sales * .06
    result1 = "{:.2f}".format(result)
    print("Sales tax of", sales, "is", result1)
    another = input("Would you like to calculate more tax(Yes/No)?")

    if another.lower() != 'yes':
        break
