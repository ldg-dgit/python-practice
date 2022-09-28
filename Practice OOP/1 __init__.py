class Player:
    # class 안에 있는 모든 메서드는 self를 가장 첫 번째 parameter로 한다.
    def __init__(self, name, xp):
        self.name = name
        self.xp = xp

    def say_hello(self):
        print(f"hello, my name is {self.name}")


bobby = Player("bobby", 1000)
print(bobby.name, bobby.xp)
bobby.say_hello()
