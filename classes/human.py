class Human:
    def __init__(self, first_name, last_name, age = 0):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age # or self._age = 0 and property on top canbe only {age}

        print("Finish generating 1 human")

    def __repr__(self):
        return f"specie: Human\n name: {self.last_name}, {self.first_name}\n age {self._age} year-old"
    
    def say_full_name(self):
        print(f'Human full-name: {self.first_name} {self.last_name}')

    def happy_birthday(self):
        self._age += 1
        print(self._age)

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        raise TypeError('Quit lying about your age!')


luke = Human("Luke", "Skywalker")
print(luke)
luke.happy_birthday()

luke.happy_birthday()

# luke.age = 4
print(luke)