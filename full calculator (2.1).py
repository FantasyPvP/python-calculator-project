equation = input()
import math
y = 0

instruction_list = ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
operation_list = []
number_list = []
total_length = len(equation)

for i in range(total_length):
    instruction_list[i] = equation[i]

for i in range(total_length):
    if str(instruction_list[i]).isnumeric():
        if str(instruction_list[i+1]).isnumeric():
            instruction_list[i+1] = instruction_list[i] + instruction_list[i+1]
            instruction_list[i] = "empty"

for i in range(total_length):
    if str(instruction_list[i]).isnumeric():
        x = 0
    else:
        if instruction_list[i] == instruction_list[i+1]:
            instruction_list[i+1] = instruction_list[i] + instruction_list[i+1]
            instruction_list[i] = "empty"


for i in range(total_length):
    if instruction_list[i].isnumeric():
        number = float(instruction_list[i])
        number_list.append(number)
    elif instruction_list[i] == "s":
        operation_list.append("sqrt")
    else:
        if instruction_list[i] == "empty":
            x = 0
        else:
            operation = instruction_list[i]
            operation_list.append(operation)

operations = len(operation_list)
operation_list.append(x)
number_list.append(x)

for i in range(operations):
    if operation_list[i] == "sqrt":
        number_list[i] = math.sqrt(number_list[i])
        print("works")
        print(number_list[i+1])
        y = y + 1

print("part 2")
total = number_list[0]

for i in range(operations):
    if operation_list[i] == "+":
        total = total + number_list[i + 1]
    elif operation_list[i] == "-":
        total = total - number_list[i + 1]
    elif operation_list[i] == "*":
        total = total * number_list[i + 1]
    elif operation_list[i] == "/":
        total = total / number_list[i + 1]
    elif operation_list[i] == "//":
        total = total // number_list[i + 1]
    elif operation_list[i] == "%":
        total = total % number_list[i + 1]
    elif operation_list[i] == "**":
        total = total ** number_list[i + 1]
    print("so far", total)
    
print(total)

