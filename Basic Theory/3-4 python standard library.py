from random import randint

user_choice = int(input("Choose number."))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("Toy won!")

elif user_choice > pc_choice:
    print("Lower! Computer chose", pc_choice)

elif user_choice < pc_choice:
    print("Higher! Computer chose", pc_choice)


# 언어에 이미 미리 포함되어 있는 함수가 standard library이다
# 엄청나게 많은 함수들이 정의되어 있지만 소수의 함수를 제외하고는 import를 해야한다.
