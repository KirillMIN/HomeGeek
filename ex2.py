
class Road:
    _mas_asphalt = 500
    _thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_check(self):
        mass = self._length * self._width * Road._mas_asphalt * Road._thickness
        return print(f'mass of asphalt: {mass} tones')


village_road = Road(1000, 500)
village_road.mass_check()





