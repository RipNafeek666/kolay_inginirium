class Car:
    def __init__(self, color, mark, max_speed, weight):
        self.color = color
        self.mark = mark
        self.max_speed = max_speed
        self.weight = weight

    def sound(self):
        print("BEEP")

    def long_sound(self):
        print('BEEB-BEEP')
lamba = Car('чёрная', 'навероное Ламба', '99999999999999999999999999999 км/с', '999кг')

lamba.sound()
lamba.long_sound()
    
print(lamba.color)
print(lamba.mark)
print(lamba.max_speed)
print(lamba.weight)