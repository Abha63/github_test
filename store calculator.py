# How to Create An Indian Kirana Store Calculator & Receipt Generator In Basic Python?
print("Welcome to our store calculator")
sum = 0
while(True):
     userInput = input("Enter the item price or q to exit\n")
     if (userInput!="q"):
         sum = sum + int(userInput)
         print(f"your total bill upto now is {sum}")
     else:
         print(f"your total bill up to now is {sum}! Thanks for shopping")
         break

