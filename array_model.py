import array
import random
numbers=array.array('i',[10,20,30,40])
print(numbers[1])
n=len(numbers)
if (n == 4):
    numbers.append(random.randint(1,100))
print(numbers)



