# ARS Gems Store sells different varieties of gems to its customers.

# Write a Python program to calculate the bill amount to be paid by a customer 
# based on the list of gems and quantity purchased.
# Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount.
# If any gem required by the customer is not available in the store, then consider total bill amount to be -1.
# Assume that quantity required by the customer for any gem will always be greater than 0.



def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    discount = 0.05
    #Write your logic here
    for i in range(len(reqd_gems)):
        gem = reqd_gems[i]
        quantity = reqd_quantity[i]
        if gem in gems_list:
            #add to bill with quantity
            price_index = gems_list.index(gem)
            gem_price = price_list[price_index]
            bill_amount += gem_price * quantity
        else:
            return -1
    #5% discount on more than 30000
    if bill_amount >30000:
        print("Without discount", bill_amount)
        discounted_amount = bill_amount * discount
        bill_amount -= discounted_amount
    return bill_amount
 
#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
 
#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]
 
#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]
# reqd_gems=["random"]
 
#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]
 
bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)