def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice =add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

#f"{변수명}" 을 하면 알아서 중괄호 + 변수명 부분을 변수 갑으로 바꾸어 준다.(문자열에 변수 넣는 방법)
#return은 함수를 끝낸다. 그 다음 함수 안 코드는 실행되지 않음