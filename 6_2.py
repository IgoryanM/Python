class Road:
    def __init__(self, _length, _width):
	    self._length = _length
	    self._width = _width

    def new_road(self, mass, thickness):
        self.mass = mass
        self.thickness = thickness
        self.all_mass = (self._length * self._width * self.mass * self.thickness) / 1000
        print(self.all_mass)

r = Road(20, 5000)
r.new_road(25, 5)