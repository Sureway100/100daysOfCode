# fruits = ["apple", "cucumber", "oranges"]

# for fruit in fruits:
#     print(fruit)

# # ages = [3, 4, 5, 6, 12, 45, 6, 77, 12, 12]
# ages = input("list of ages ").split()
# # print(ages)

# totalAge = 0

# for age in ages:
#     totalAge += int(age)
#     print(totalAge)

# print("total ages ", totalAge)
# print("ave ages ", totalAge / len(ages))


# # highest score in an array
# items = [23, 45, 12, 99, 41]

# highest_num = 0
# for item in items:
#     if item > highest_num:
#         highest_num = item
# print("highest score is ", highest_num)


# for loops with the range from 1 to 10
# for num in range(1, 11):
#     print(num)
# for num in range(1, 21, 2):  # here is start, end, incrementor
#     print(num)


# fizzBuzz

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("fizzBuzz")
    else:
        print(num)
