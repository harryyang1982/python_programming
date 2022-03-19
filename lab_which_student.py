# -*- coding: utf-8 -*-

year = int(input("Which year were you born? "))
age = 2022 - year + 1

if age >= 20 and age < 26:
    print("대학생")
elif age >= 17:
    print("고등학생")
elif age >= 14:
    print("중학생")
elif age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다.")


