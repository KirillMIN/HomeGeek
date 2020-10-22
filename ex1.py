from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ["red", "yellow", "green"]

    @staticmethod
    def running(number):
        count = 0
        for item in cycle(TrafficLight.__color):
            print(f'Traffic light switches: {item}')
            if item == "red":
                sleep(7)
            elif item == "yellow":
                sleep(2)
            elif item == "green":
                sleep(5)
            if count > number:
                break
            count += 1


number = int(input("how many:"))
Traffic = TrafficLight()
Traffic.running(number)
