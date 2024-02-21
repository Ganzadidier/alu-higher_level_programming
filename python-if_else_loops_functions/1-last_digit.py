#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number_str_version = str(number)

Last_digit_of_number = number_str_version[-1]


if int(Last_digit_of_number) >5:
	print(f"Last digit of {number:d} is {Last_digit_of_number} and is greater than 5")

elif int(Last_digit_of_number) ==0:
	print(f"Last digit of {number:d} is {Last_digit_of_number} and is 0")

elif (int(Last_digit_of_number) < 6) & (int(Last_digit_of_number) !=0):
	print(f"Last digit of {number:d} is {Last_digit_of_number} and is less than 6 and not 0")
