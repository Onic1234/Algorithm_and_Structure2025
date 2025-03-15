class Vehicle:
    def __init__(self, name, color, year_production, capacity, mileage):
        """Initialize the vehicle with name, color, year of production, capacity, and mileage."""
        self.name = name
        self.color = color
        self.year_production = year_production
        self.capacity = capacity
        self.mileage = mileage

    def set_capacity(self, capacity):
        """Set the capacity of the vehicle."""
        self.capacity = capacity

class Truck(Vehicle):
    def __init__(self, name, color, year_production, capacity, mileage):
        """Initialize the truck with the same attributes as the vehicle."""
        super().__init__(name, color, year_production, capacity, mileage)

# Example usage
vehicle1 = Vehicle("Car", "Red", 2020, 5, 15000)
print(f"Vehicle: {vehicle1.name}, Color: {vehicle1.color}, Year: {vehicle1.year_production}, Capacity: {vehicle1.capacity}, Mileage: {vehicle1.mileage}")

truck1 = Truck("Truck", "Blue", 2018, 3, 30000)
print(f"Truck: {truck1.name}, Color: {truck1.color}, Year: {truck1.year_production}, Capacity: {truck1.capacity}, Mileage: {truck1.mileage}")

# Set new capacity for the truck
truck1.set_capacity(4)
print(f"Updated Truck Capacity: {truck1.capacity}")

print('\n--- Oleh L200234275 ---')