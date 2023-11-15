#calculating my losses

#how much did i spend?
spent = float(input('\nHow much did you spend on crypto?:\t'))

usdt = float(input("\nWhat is the price of 1 USDT in your local currency?:\t"))

#what was the price of the token?
tokens = float(input("\nHow many tokens do you have?:\t"))

#how much money can i afford to lose?
willing = float(input("\nHow much are you willing to lose?: \t"))



#total amount of money i expect to lose
remainder_after_loss = spent - willing

price_at_loss = remainder_after_loss/tokens
usdt_price_at_loss = price_at_loss/usdt

print(f"\n\nPlace your limit order at {usdt_price_at_loss:.6} ({price_at_loss:.2f})")



#output is the sell order place...