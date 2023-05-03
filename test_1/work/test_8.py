


class Car :
    def __init__(self,model,color,speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self,up):
        self.speed += up
        if self.speed >455:
            self.speed = 455

    def brake(self,down):
        self.speed -= down
        if self.speed < 0:
            self.speed = 0
    
    def get_speed(self):
        return self.speed


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def speak(self):
        pass
class Dog:

    def speak(self):
        print("왈왈")

class Cat(Animal):

    def speak(self):
        print("냐냐")



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def get_area(self):
        print(f"π{self.radius}^2:둥글넓이다!!")


class Rectangle(Shape):
    def __init__(self,length,widht):
        self.length = length
        self.widht = widht

    def get_area(self):
        print(f"{self.length},{self.widht}를(을)곱하면 넓이다!")

