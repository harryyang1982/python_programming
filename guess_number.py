# -*- coding: utf-8 -*-

import random

guess_number = random.randint(1, 100)

user_input = int(input("숫자를 맞혀 보세요. (1~100) \n"))
while (user_input is not guess_number):
    if user_input > guess_number:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    user_input = input("다시 입력하세요. \n")
else:
    print("정답입니다. 입력한 숫자는", user_input, "입니다!")