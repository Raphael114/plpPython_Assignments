class Vehicle:
    def move(self):
        print("This vehicle moves in its own way.")

class Car(Vehicle):
    def move(self):
        print("Car is Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print(" Plane is Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Boat is Sailing 🚤")

# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()