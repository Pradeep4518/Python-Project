U,A = map(float,input("Enter the velocity and accleration:").split())
t = int(input("Enter the time: " ))
d = U * t + A *( t ** 2)
print("Distance travelled = ",d)
