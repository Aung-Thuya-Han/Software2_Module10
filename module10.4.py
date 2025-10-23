import random

class Car:
    def __init__(self, name):
        self.name = name
        self.distance_travelled = 0
        self.speed = random.randint(100, 200)  # initial speed km/h

    def drive(self):
        self.distance_travelled += self.speed

    def change_speed(self):
        self.speed += random.randint(-10, 15)  # speed change



class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars = cars_list

    def hour_passes(self):
        for car in self.cars:
            car.change_speed()
            car.drive()

    def print_status(self):
        print(f"{'Car':10} {'Distance Travelled':>24}")
        for car in self.cars:
            print(f"{car.name:10} {car.distance_travelled:>20} km")

    def race_finished(self):
        for car in self.cars:
            if car.distance_travelled >= self.distance:
                return True
        return False


cars_list = []
for i in range(1, 11):
    car = Car("Car" + str(i))
    cars_list.append(car)

race = Race("Grand Demolition Derby", 8000, cars_list)

hours = 0
while race.race_finished() != True:
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nAfter {hours} hours:")
        race.print_status()

print("\nFinal status:")
race.print_status()
