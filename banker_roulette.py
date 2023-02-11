names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random
person=random.choice(names)
print(person)