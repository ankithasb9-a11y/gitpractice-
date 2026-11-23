# Your shopping cart contains three products. Their prices are ₹500, ₹1,200 and ₹2,000, and their respective quantities are 2, 1 and 3.

# prices = [500,1200,2000]
# quantities = [2,1,3]

# amount  = 500*2 + 1200*1 + 2000*3
# print(amount)

# A project management API receives 120 total tasks, out of which 90 are completed. You need to calculate the completion percentage.
# total_task = 120
# completed_task = 90 
# compeletion_percentage = (completed_task/total_task)*100
# print(compeletion_percentage)



# Order of ₹5,000 with 20% discount and 5% GST. Print the final amount.

# order = 5000
# discount = 20
# gst = 5

# discount_amount = 5000*20/100
# price_after_discount = order - discount_amount
# tax = price_after_discount*gst/100
# final_amount = price_after_discount + tax
# print(final_amount)

# An e-commerce application receives an order worth ₹10,000. The customer receives a 10% discount, followed by 18% tax on the discounted amount. final

# order = 10000
# discount = 10
# tax = 18

# discount_amount = order*discount/100
# price = order - discount_amount
# tax_pay = price*tax/100
# final_price = price + tax_pay
# print(final_price)

# discount_amount = order_amount * discount_percent / 100
# discounted_amount = order_amount - discount_amount
# tax_amount = discounted_amount * tax_percent / 100
# final_amount = discounted_amount + tax_amount




# A product costs ₹800 and sells for ₹1,000. Print profit and profit %.
# profit = 1000-800
# profit_per = profit/800*100
# print(profit_per)



# even/odd

new = int(input("enter the number\n"))
if new % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")
