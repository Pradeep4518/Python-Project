P,T,R = map(float,input("Enter the principal , time and rate if interest").split())
CI = P*((1 + (R/100))**T)- P
print("Compund interest = ",CI)
