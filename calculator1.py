# -*- coding: utf-8 -*-

user_input = int(input("구구단 몇 단을 계산할까? "))
print("구구단", user_input, "단을 계산한다. \n")
for i in range(1, 10):
    print(user_input, "X", i, "=", user_input * i)