from random import *
numbers=[]
while len(numbers) !=7:
    num= randint(1, 399)
    if num not in numbers:
        numbers.append(num)
numbers.sort()
print("the selected number: %s" % numbers)

