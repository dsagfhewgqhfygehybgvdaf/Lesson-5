buyprice=int(input("Enter the buy price:$ "))
sellprice=int(input("Enter the sell price:$ "))
if sellprice>buyprice:
    profit=sellprice-buyprice
    print("Profit of:$", profit)
elif sellprice<buyprice:
    loss=buyprice-sellprice
    print("Loss of:$", loss)
else:
    print("No profit, no loss")