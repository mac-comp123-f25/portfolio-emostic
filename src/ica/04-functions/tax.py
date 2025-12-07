def add_tax(price, tax_rate):
    print('the inputs are:', price, tax_rate)
    tax_amt = price * tax_rate
    print('the tax amount is:', tax_amt)
    return price + tax_amt

'''
Local environment
price 25.99
tax_rate 0.0725
tax_amt 1.88
'''

add_tax(25.99, 0.0725)
print(add_tax(25.99, 0.0725))
