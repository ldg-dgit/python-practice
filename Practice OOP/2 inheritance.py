class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello, my name is {self.name}")


class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp


class Fan(Human):
    def __init__(self, name, favorite_team):
        super().__init__(name)
        self.favorite_team = favorite_team


bobby_player = Player("bobby", 100)
bobby_player.say_hello()
bobby_fan = Fan("bobby_fan", "korea")
bobby_fan.say_hello()
