#Módulo random
import random

numbers_lottery = range(60)
print(random.sample(numbers_lottery,6))

two_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(two_with_replacement)

my_friends = ["Aline","Gabriel","Bianca"]
print(random.choice(my_friends))
