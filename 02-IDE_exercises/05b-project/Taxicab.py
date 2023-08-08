class Taxicab:
    """
    Represents a taxi whose coordinates and odomoter are measured.
    """
    def __init__(self, x_coord: int, y_coord: int, odometer:int = 0):
        """
        Creates a new vehicle in the class Taxicab.
        """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.odomoter = odometer
    def get_x_coord(self):
        """
        Provides the taxi's current x coordinate.
        """
        return self.x_coord
    
    def get_y_coord(self):
        """
        Provides the taxi's current y coordinate.
        """
        return self.y_coord
    def get_odometer(self):
        """
        Provides the total units of measurement moved by the taxi
        """
        return self.odomoter
    def move_x(self, units: int):
        """Moves the taxi left or right depending on the total number of units provided"""
        self.x_coord += units
        self.odomoter += abs(units)
    def move_y(self, units: int):
        """Moves the taxi up or down depending on the total number of units provided"""
        self.y_coord += units
        self.odomoter += abs(units)
cab = Taxicab(3, -8)       # creates a Taxicab object at coordinates (3, -8)
cab.move_x(4)              # moves cab 4 units "right"
cab.move_y(-5)             # moves cab 5 units "down"
cab.move_x(-2)             # moves cab 2 unit "left"
print(cab.get_odometer())  # prints the current odometer reading