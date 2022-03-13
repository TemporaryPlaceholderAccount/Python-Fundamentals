class Watch:
    def __init__(self, Waterproof, Analogue, Size):
        self.Waterproof = Waterproof
        self.Analogue = Analogue
        self.Size = Size

    def watch_start_stop(self):
        print(str.format("Do {0} it work doe?", self.Size))

    def get_Waterproof(self):
        return self.Waterproof

    def set_Waterproof(self, bre):
        self.Waterproof = bre
        
    def get_Analogue(self):
        return self.Analogue

    def set_Analogue(self, run):
        self.Analogue = run

    def get_seats(self):
        return self.seats

    def set_seats(self, Size):
        self.seats = Size

watch = Watch("yes", 1, 100)
print(watch.Size)
print(watch.watch_start_stop)

