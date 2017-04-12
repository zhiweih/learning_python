class Animal:
    def reply(self):
        self.speak()

class Mammal(Animal):
    def speak(self):
        print("我要吃奶！")

class Cat(Mammal):
    def speak(self):
        print("喵")

class Dog(Mammal):
    def speak(self):
        print("汪汪")

class Primate(Mammal):
    def speak(self):
        print("脑子是个好东西")

class Hacker(Primate):
    def speak(self):
        print("Hello World!")
