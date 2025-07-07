bill = int(input("what is your total bill?"))
tip = int(input("how much do you wanna pay for tip 10 12 15"))
people = int(input("how many people invited?"))
total_tip_per_person = (tip / 100 * bill ) / people
print(f"you should pay : {total_tip_per_person}")