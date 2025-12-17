age = int(input("Please enter your age:"))

total = 0

for number in range(1, age + 1):
    total += number

print(f'The sum of all numbers from 1 to {age} is: {total}')