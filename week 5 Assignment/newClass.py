class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def take_photo(self):
        if self.is_on:
            print(f"{self.brand} {self.model} takes a photo!")
        else:
            print("Please turn on the phone first.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}mAh)"


# Inheritance: A subclass for a specific type of smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system  # e.g., "liquid", "fan"

    def launch_game_mode(self):
        if self.is_on:
            print(f"{self.brand} {self.model} is now in Game Mode with {self.cooling_system} cooling!")
        else:
            print("Please turn on the phone to launch Game Mode.")

    # Polymorphism: override take_photo
    def take_photo(self):
        if self.is_on:
            print(f"{self.brand} {self.model} takes a high-res gaming screenshot!")
        else:
            print("Please turn on the phone first.")


# Example usage:
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S21", 128, 4000)
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 6000, "liquid")

    phone.power_on()
    phone.take_photo()
    phone.power_off()

    gaming_phone.power_on()
    gaming_phone.launch_game_mode()
    gaming_phone.take_photo()
    gaming_phone.power_off()