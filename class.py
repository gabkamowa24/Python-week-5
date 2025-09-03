# Assignment 1: Design Your Own Class

class House:
    def __init__(self, address, num_rooms, color):
        self.address = address
        self.num_rooms = num_rooms
        self.color = color
    
    def describe(self):
        return f"This is a {self.color} house at {self.address} with {self.num_rooms} rooms."
    
    def paint(self, new_color):
        self.color = new_color
        return f"The house has been painted {new_color}."


# Inheritance Example: SmartHouse extends House
class SmartHouse(House):
    def __init__(self, address, num_rooms, color, wifi_enabled=True):
        super().__init__(address, num_rooms, color)  # call parent constructor
        self.wifi_enabled = wifi_enabled
    
    # Override describe() for polymorphism
    def describe(self):
        wifi_status = "with Wi-Fi automation" if self.wifi_enabled else "without smart features"
        return f"This is a {self.color} smart house at {self.address} with {self.num_rooms} rooms, {wifi_status}."


# Example usage
basic_house = House("123 Main St", 3, "blue")
print(basic_house.describe())
print(basic_house.paint("green"))

smart_home = SmartHouse("456 Tech Ave", 5, "white")
print(smart_home.describe())
