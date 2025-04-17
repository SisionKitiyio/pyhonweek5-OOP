class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self.secret_identity = secret_identity
        self.power_level = power_level  

    def introduce(self):
        print(f"I am {self.name}! (Secretly: {self.secret_identity})")

    def use_power(self):
        print(f"{self.name} uses their power at level {self.power_level}!")

    def __str__(self):
        return f"Superhero: {self.name} | Power: {self.power_level}/10"


# Inherited Class (Polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, power_level, max_altitude):
        super().__init__(name, secret_identity, power_level)
        self.max_altitude = max_altitude  

    def use_power(self):  
        print(f"{self.name} soars at {self.max_altitude}m with a sonic boom! ✈️")

    def patrol_sky(self):
        print(f"{self.name} is scanning the city from above!")



if __name__ == "__main__":
    hero1 = Superhero("Captain Code", "Lily", 8)
    hero2 = FlyingHero("Sky Guardian", "john", 9, 2000)

    hero1.introduce()       
    hero1.use_power()       

    hero2.introduce()       
    hero2.use_power()       
    hero2.patrol_sky()

    class Vehicle:
        def __init__(self, name):
            self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must define move()!")


class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road! ")


class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying through the sky! ")


class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water! ")



if __name__ == "__main__":
    vehicles = [
        Car("Tesla Model S"),
        Plane("Boeing 747"),
        Boat("Titanic II")
    ]

    for vehicle in vehicles:
        vehicle.move() 