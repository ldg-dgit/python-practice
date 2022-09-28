class Dog:
    def __init__(self, name):
        self.name = name

    # 이 문자열 출력되도록 한다. 원래는 값의 메모리 위치를 출력한다.
    # 우리는 오버라이딩 한 것이다. str으로
    def __str__(self):
        print(super().__str__())
        return f"Dog : {self.name}"


tata = Dog("tata")
print(tata)

# dir은 클래스의 속성과 메서드들을 모두 보여준다

print(dir(tata))
