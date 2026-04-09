hotel_name = "King's Hotel"
def calculate_bill (room_charges,food_charge,service_charge):
    total = room_charges + food_charge + service_charge
    return total
def apply_discount(total_amount):
    if total_amount > 5000 :
        discount_percentage = 15
        discoun_price = (discount_percentage / 100)*total_amount
        final_bill = total_amount - discoun_price
        return final_bill
    else:
        return total_amount
def display_bill(guest_name,total_bill):
    print(f"Hotel : {hotel_name}")
    print(f"Guest : {guest_name}")
    print(f"Bill : {total_bill}")

guest = input("Enter the Guest name: ")     
room_service = int(input("Enter the Room charges :"))
food_service = int(input("Enter the Food charges :"))
service_charges = int(input("Enter the Service charges :"))
total = calculate_bill(room_service,food_service,service_charges)
payable_amount = apply_discount(total)
display_bill(guest,payable_amount)



    
    
