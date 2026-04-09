#Question 1:
#Scenario:A company gives bonuses based on employee salary.
#Task:Write a Python program to calculate the bonus amount using given rules.
salary = int(input("Enter salary: "))

if salary > 0:
    bonus = salary * 0.07
    print("Bonus =", int(bonus))
else:
    print("Invalid salary")
