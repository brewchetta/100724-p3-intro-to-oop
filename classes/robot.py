class Robot:
    
    def __init__(self, name, wd40="8oz"):
        # print("HELLO I AM MAKING A ROBOT")
        # print("I AM:", self)
        self.name = name
        self.wd40 = wd40
        self.battery_life = 100

    def __repr__(self):
        return f"Robot(name={self.name}, battery_life={self.battery_life}, wd40={self.wd40})"
    
    def build(self, item):
        return f"Hello my name is {self.name} and I am building some good quality {item}"
    
    @property # GETTER
    def battery_life(self):
        return f"{self._battery_life}%"
    
    @battery_life.setter # SETTER
    def battery_life(self, value):
        if type(value) == int and 100 >= value >= 1:
            self._battery_life = value
        else:
            raise TypeError("battery_life must be and integer between 100 and 1 inclusive")
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise TypeError("You may not rename this bot")
        else:
            self._name = value