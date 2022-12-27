class Animals:
    def __init__(self, name, type, gender, weight):
        self.name = name
        self.type = type
        self.gender = gender
        self.weight = weight

    def move(self, distantion, direction):
        print(self.name + ' moved ' + distantion + ' to the ' + direction)

    def eat(self, food):
        print(self.name + ' ate ' + food)


class Mammals(Animals):
    def __init__(self, name, kind, gender, weight, coat_color):
        super().__init__(name, kind, gender, weight)
        self.coat_color = coat_color

    def do(self):
        print(f'{self.name} doing something')

class Human(Mammals):
    def __init__(self, name, kind, gender, weight, coat_color, eyes_color, profession):
        super().__init__(name, kind, gender, weight, coat_color)
        self.eyes_color = eyes_color
        self.profession = profession

    def writting_code(self):
        print(f'{self.name} doing something....')

class Dog(Mammals):
    def __init__(self, name, kind, gender, weight, coat_color, owner):
        super().__init__(name, kind, gender, weight, coat_color)
        self.owner = owner

    def play(self):
        print(f'{self.name} is playing with toy')

class Cat(Mammals):
    def __init__(self, name, kind, gender, weight, coat_color, favorite_toy):
        super().__init__(name, kind, gender, weight, coat_color)
        self.favorite_toy = favorite_toy

    def play(self):
        print(f'{self.name} is playing with {self.favorite_toy}')

class Student(Human):
    def __init__(self, name, kind, gender, weight, coat_color, eyes_color, profession, hw_count):
        super().__init__(name, kind, gender, weight, coat_color, eyes_color, profession)
        self.hw_count = hw_count

    def study(self):
        print(f'{self.name} is studing statistics')

    def __eq__(self, student):
        return self.hw_count == student.hw_count

bear = Animals('Mishka', 'Bear', 'Male', 500)
bear.eat('fish')

tiger = Mammals('Amur', 'Tiger', 'Male', 750, 'Orange')
tiger.eat('rabbit')
tiger.do()

human = Human('Ivan', 'Human', 'Male', 85, 'White', 'Blue', 'accountant')
human.writting_code()

cat = Cat('Liza', 'Cat', 'Female', 7, 'Grey', 'Сouch')
cat.play()

dog = Dog('Richard', 'Dog', 'Male', 9, 'Ginger', 'Denis')
dog.play()

stud1 = Student('Eugene', 'Human', 'Male', 79, 'White', 'Green', 'Student', 20)
stud2 = Student('Anna', 'Human', 'Female', 68, 'White', 'Blue', 'Programmer', 5)

print(stud1 == stud2)
