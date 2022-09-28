# 언제나 init 메서드를 만들 필요는 없다.
class Dog:
    def woof(self):
        print("woof woof")


class Beagle(Dog):
    def woof(self):
        super().woof()
        print("super woof")


# 오버라이딩
class SuperBeagle(Dog):
    def woof(self):
        print("super woof")


beagle = Beagle()
beagle.woof()
