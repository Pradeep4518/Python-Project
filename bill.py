Rice_price , Rice_quantity = map(float,input("Enter the Price and quantity of Rice : ").split())
oil_price , oil_quantity = map(float,input("Enter the Price and quantity of oil : ").split())
soap_price , soap_quantity = map(float,input("Enter the Price and quantity of Soap : ").split())
total = Rice_price*Rice_quantity + oil_price*oil_quantity + soap_price*soap_quantity
member = input("Is the customer is already a member : ")#if he/she was give yes else no
discount = 0
if(member == "yes"):
    member = 1
elif(member == "no"):
    member = 0
if(member):
    if(total >= 800):
        discount = total * 0.20
    
else:
    if(total >= 500):
        discount = total * 0.10
coupon = input("Enter the COUPON CODE: ").upper()
valid_coupons = ["SAVE10","SAVE20","SAVE30"]
if coupon == "SAVE10":
    coupon_discount = 10
if coupon == "SAVE20":
    coupon_discount = 20
if coupon == "SAVE30":
    coupon_discount = 30

total1 = (total - discount) - coupon_discount
gst = total1 * 0.05
bill = total1 + gst

print("The total Bill : ",bill)
    
         
