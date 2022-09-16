print("Welcome to the tip calculator!")
bill = input("What was the total bill?")
tip = input("How much tip would you like to give? 10, 12, 15?")
people = input("How many pepople to split the bill?")
percent = (float(tip)/100)+1
output = (float(bill)/int(people))*percent
final = round((output),3)
print(f"Each person should pay: {final} $")