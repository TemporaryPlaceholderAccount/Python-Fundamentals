class Boat:
    def __init__(self, Hull_color, Materials, Size):
        self.Hull_color = Hull_color
        self.Materials = Materials
        self.Size = Size

    def boat_start_stop(self):
        print(str.format("Do {0} it work doe?", self.Size))

    def get_Hull_color(self):
        return self.Hull_color

    def set_Hull_color(self, bre):
        self.Hull_color = bre
        
    def get_Materials(self):
        return self.Materials

    def set_Materials(self, run):
        self.Materials = run

    def get_seats(self):
        return self.seats

    def set_seats(self, Size):
        self.seats = Size

boat = Boat("chartreuse", 1, 100)
print(boat.Size)
print(boat.boat_start_stop)
