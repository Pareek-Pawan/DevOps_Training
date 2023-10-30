# 1st input: enter height in meters e.g: 1.65
height = input("Enter the Height : \n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter the Weight : \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
H1 = float(height)
W1 = int(weight)
Bmi = W1/(H1*H1)
Bmi1 = int(Bmi)
print(Bmi1)