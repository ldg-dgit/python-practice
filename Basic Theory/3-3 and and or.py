age = int(input("How old are you?"))

if age < 18:
    print("You can't drink.")

elif age >= 18 and age <= 35:
    print("You are young.")

elif age == 60 or age == 70:
    print("Party!!")

else:
    print("Go ahead.")

# type함수는 변수 타입을 알 수 있다.
# user가 input에 입력한 것들은 string으로 받는다.
# int() 이렇게 감싸서 formatting을 해야한다.
