print("mini calculator")
num1 = float(input("enter your first number"))
num2= float(input("enter your second  number"))
print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplecation \npress 4 for division")
choise=int(input("enter your choice from  1-4"))
if choice == 1:
 print (num1 + num2)
elif choice == 2:
 print(num1 - num2)
elif choice == 3:
 print(num1 * num2)
elif  choice == 4:
 print(num1 / num2)
else:
 print("invalid input")