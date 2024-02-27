class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = self.height*self.pi*(self.radius)**2
        print(volume)
        return volume


    def surface_area(self):
        surface = 2 * (self.pi * self.radius ** 2) + (2 * self.pi * self.radius * self.height)
        print(surface)
        return surface

# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
c.surface_area()