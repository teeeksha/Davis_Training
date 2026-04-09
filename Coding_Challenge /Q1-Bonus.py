#Question 1:
#Scenario:A company gives bonuses based on employee salary.
#Task:Write a Python program to calculate the bonus amount using given rules.
# Take salary input from user
salary = int(input("Enter salary: "))

# Check valid salary
if salary > 0:
    # Calculate 7% bonus
    bonus = salary * 0.07
    print("Bonus =", int(bonus))
else:
    print("Invalid salary")
