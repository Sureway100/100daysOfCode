# strings------------------------
print("hello"[0])  # this is called subscripting
# interger
print(123_456_789)
# float----------------------------
print(3.12345)
# boolean--------------------------------
print(True)  # not print(true)
print(False)

# type checking---------------------------------
print(type("i am here"))
print(type(1234))
print(type(True))

# type conversion or type casting----------------------------
# len_num = len(input("what is your name"))
# con_len = str(len_num)
# print("my name is " + con_len)

# operation using PEMDAS-------------------------

# 5 + 7
# 4 / 2
# 3 // 2     #this, you will get interger immediately, discarding float numbers
# 2 ** 3  # power
# 2 * 5
# 5 - 4

# BMI Calculator ------------------------------------------
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# height1 = float(height)
# weight1 = float(weight)

# result = float(weight1) / (height1 ** 2)
# print(int(result))


# number manipulation and F string---------------------------
print(round(8/3))
print(round(8/3, 2))
print(round(2.6666666666667, 3))

# F strings => this helps incorporate things that have different data types-----------------------
# BEFORE we introduced F strings
score = 20.9
print("your total score is " + str(score))
# AFTER
print(f"your total score is {score}")
