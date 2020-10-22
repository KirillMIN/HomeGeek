class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self. name = name
        self. is_police = is_police

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')

    @staticmethod
    def go():
        print("Car  is moving")

    @staticmethod
    def stop():
        print("Car is standing")

    @staticmethod
    def turn(direction):
        print(f'Car is turning: {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('over speed')
        print(f'{self.name} speed: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('over speed')
        print(f'{self.name} speed: {self.speed}')


Volga = TownCar(70, 'red', 'Volga', False)
Volga.show_speed()
Volga.stop()
Volga.turn('left')
Volga.go()
