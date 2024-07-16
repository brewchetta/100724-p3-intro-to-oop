class Human:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    def __repr__(self):
        return f"Human(first_name={self.first_name}, last_name={self.last_name}, age={self.age})"
    
    def say_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property # GETTER
    def age(self):
        return self._age
    
    @age.setter # SETTER
    def age(self, value):
        if hasattr(self, 'age'):
            raise TypeError("Quit lying about your age!")
        elif type(value) == int:
            self._age = value
        else:
            raise TypeError("Age must be an integer")

    def happy_birthday(self):
        self._age += 1