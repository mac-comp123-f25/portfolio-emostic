money = 732

print("Making change for", money, "cents:")

#dollars
dollars = money // 100
money = money % 100

#quarters
quarters = money // 25
money = money % 25

#dimes
dimes = money // 10
money = money % 10

#nickels
nickels = money // 5
money = money % 5

#pennies
pennies = money

print(" Dollars:", dollars)
print(" Quarters:", quarters)
print(" Dimes:", dimes)
print(" Nickels:", nickels)
print(" Pennies:", pennies)
