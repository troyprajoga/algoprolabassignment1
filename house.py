# pranav harish nathani (2702293872), troy poetra prajoga (2702291910)

class House:
    total_house = 0

    def __init__(self, floors, doors, windows, color, has_garage, address):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.address = address

        House.total_house += 1

    def display_info(self):
        # Display information
        print("House information: ")
        print(f"      -Address: {self.address}")
        print(f"      -Doors: {self.doors}")
        print(f"      -Floors: {self.floors}")
        print(f"      -Windows: {self.windows}")
        print(f"      -Color: {self.color}")
        print(f"      -Garage: {'Yes' if self.has_garage else 'no'}")

    @classmethod
    def display_total_house(cls):
        print(f"Total number of houses = {cls.total_house}")

    @staticmethod
    def validate_house(house):
        if not isinstance(house, House):
            return False  # not a valid house object
        if not all(isinstance(attr, int) and attr > 0 for attr in (house.floors, house.doors, house.windows)):
            return False  # floors, doors, windows should be positive int

        return True

    @staticmethod
    def paint_house(house):
        inputs = input()
        if inputs == "yes":
            print("what color do u want to change it to")
            newcol = input()
            house.color = newcol
            house.display_info()


house1 = House(floors=2, doors=3, windows=6, color="Blue", has_garage=True, address="123 Main st.")
house2 = House(floors=3, doors=3, windows=9, color="yellow", has_garage=False, address="123 Main st.")

house1.display_info()
print()
house2.display_info()
House.display_total_house()

validation_result = House.validate_house(house2)
print(f"House Validation Result: {'Valid' if validation_result else 'Invalid'}")

correct = False


def selecting_house():
    print("which house would you like to change(1 or 2)\n")
    house_to_change = int(input())
    if house_to_change == 1:
        house_to_change = house1

    if house_to_change == 2:
        house_to_change = house2
    return house_to_change



while True:
    the_house = selecting_house()
    print("1. change paint color\n2. add garage?\nchange address\n=====================\n")
    userinput = int(input())
    if userinput == 1:
        House.paint_house(the_house)
    if userinput == 2:
        if the_house.has_garage == False:
            the_house.has_garage = True
            the_house.display_info()
        else:
            print("already has garage")

