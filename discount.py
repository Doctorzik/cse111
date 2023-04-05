#You work for a retail store that wants to increase 
# sales on Tuesday and Wednesday, which are the store’s 
# slowest sales days. On Tuesday and Wednesday, if a 
# customer’s subtotal is $50 or greater, the store will 
# discount the customer’s subtotal by 10%.


from datetime import datetime #This import the datetime library

subtotal = float(input("Please enter the subtotal: "))
current_date = datetime.now()

day_of_week = current_date.weekday()

if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
  promo_discount = subtotal * 0.1 
  discount = subtotal - promo_discount 
  sales_tax_amount = 0.06 * discount
  total_amount_due = sales_tax_amount  + discount 
  print(promo_discount, sales_tax_amount, total_amount_due)
else: 
  sales_tax_amount = subtotal * 0.06
  total_amount_due = sales_tax_amount + subtotal
  print(f"Sales tax amount:{sales_tax_amount:.2f}")
  print(f"Total: {total_amount_due:.2f}")

