# Write a program that checks whether a number is even or odd. 
  

A = int(input("Enter a number: "))

if A == 0:
    print("The number is zero")
elif A % 2 == 0:
    print(f"The number {A} is even")
else:
    print(f"The number {A} is odd")
