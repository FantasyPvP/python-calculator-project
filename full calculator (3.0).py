# starting variables

import math
instruction_list_unprocessed = []
instruction_list = []

# user interface

print("this is a calculator that can perform many common mathematical functions")
print("your input must be a single string of text with no spaces")
print("possible operations: +, -, *, /, //, %, **, sqrt")

# inputs and initial processing

equation = input("please enter equation...")
total_length = len(equation)

# moving each character of the equation to a separate variable in a list (instruction_list_unprocessed)

for i in range(total_length):
    instruction_list_unprocessed.append(equation[i])

instruction_list_unprocessed.append("x")
# consolidating multi digit numbers

for i in range(total_length):
    if str(instruction_list_unprocessed[i]).isnumeric():
        if str(instruction_list_unprocessed[i + 1]).isnumeric():
            instruction_list_unprocessed[i + 1] = instruction_list_unprocessed[i] + instruction_list_unprocessed[i + 1]
            instruction_list_unprocessed[i] = "empty"

# consolidating muliti character operators

for i in range(total_length):
    if str(instruction_list_unprocessed[i]).isnumeric():
        b = 0
    else:
        if instruction_list_unprocessed[i] == instruction_list_unprocessed[i + 1]:
            instruction_list_unprocessed[i + 1] = instruction_list_unprocessed[i] + instruction_list_unprocessed[i + 1]
            instruction_list_unprocessed[i] = "empty"

# consolidating sqrt command

for i in range(total_length):
    if str(instruction_list_unprocessed[i]).isalpha():
        if str(instruction_list_unprocessed[i]) == "s":
            instruction_list.append("sqrt")
    else: instruction_list.append(instruction_list_unprocessed[i])

# inputs are processed here before calculation

length = len(instruction_list)
operation_count = 0

# sqrt module

sqrt_count = instruction_list.count("sqrt")

for i in range(sqrt_count):
    x = instruction_list.index("sqrt")
    instruction_list[x] = math.sqrt(int(instruction_list[x + 1]))
    instruction_list.pop(x + 1)
    operation_count = operation_count + 2

# indices module

power_count = instruction_list.count("**")

for i in range(power_count):
    x = instruction_list.index("**")
    instruction_list[x] = int(instruction_list[x - 1]) ** int(instruction_list[x + 1])
    instruction_list.pop(x + 1)
    instruction_list.pop(x - 1)
    operation_count = operation_count + 2

# multiplication module

multiplication_count = instruction_list.count("*")

for i in range(multiplication_count):
    x = instruction_list.index("*")
    instruction_list[x] = int(instruction_list[x - 1]) * int(instruction_list[x + 1])
    instruction_list.pop(x + 1)
    instruction_list.pop(x - 1)
    operation_count = operation_count + 2

# remainder division module

remainder_div_count = instruction_list.count("%")

for i in range(remainder_div_count):
    x = instruction_list.index("%")
    instruction_list[x] = int(instruction_list[x - 1]) % int(instruction_list[x + 1])
    instruction_list.pop(x + 1)
    instruction_list.pop(x - 1)
    operation_count = operation_count + 2

# integer division module

int_div_count = instruction_list.count("//")

for i in range(int_div_count):
    x = instruction_list.index("//")
    instruction_list[x] = int(instruction_list[x - 1]) // int(instruction_list[x + 1])
    instruction_list.pop(x + 1)
    instruction_list.pop(x - 1)
    operation_count = operation_count + 2

# division module

division_count = instruction_list.count("/")

for i in range(division_count):
    x = instruction_list.index("/")
    instruction_list[x] = int(instruction_list[x - 1]) / int(instruction_list[x + 1])
    instruction_list.pop(x + 1)
    instruction_list.pop(x - 1)
    operation_count = operation_count + 2

# addition module

addition_count = instruction_list.count("+")

for i in range(addition_count):
    x = instruction_list.index("+")
    instruction_list[x] = int(instruction_list[x - 1]) + int(instruction_list[x + 1])
    instruction_list.pop(x + 1)
    instruction_list.pop(x - 1)
    operation_count = operation_count + 2

# subtraction module

subtraction_count = instruction_list.count("-")

for i in range(subtraction_count):
    x = instruction_list.index("-")
    instruction_list[x] = int(instruction_list[x - 1]) - int(instruction_list[x + 1])
    instruction_list.pop(x + 1)
    instruction_list.pop(x - 1)
    operation_count = operation_count + 2
answer = instruction_list[i]
print("your answer is:", answer)
