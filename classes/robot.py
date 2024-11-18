class Robot:

    # init is a magic method that helps assign attributes for new instances
    # can also be used for any other functionality you need when you create an instance
    def __init__(self, name:str, mobility:int):
        self.name = name
        self.mobility = mobility
        self.motive = "BE NICE TO ALL HUMANS"
        # print("INITIALIZING BEEP BOOP")
        # print(f"MY NAME IS {self.name}")
        # print(f"MY MOBILITY IS {self.mobility}")

    def flip_burger(self):
        return f"{self.name} has flipped a burger BEEP BOOP"

    def who_am_i(self):
        return self

    def __repr__(self):
        return f"Robot(name={self.name}, mobility={self.mobility}, motive={self.motive})"
    
    # GETTER
    @property
    def name(self):
        print("NAME PROPERTY IS BEING ACCESSED")
        return self._name.upper()

    # SETTER
    @name.setter
    def name(self, new_value):
        print(f"new_value is {new_value}")
        if ( isinstance(new_value, str) ):
            self._name = new_value
        else:
            raise TypeError("Robot name must be a string BEEP BOOP")
        
    # GETTER
    @property
    def motive(self):
        return self._motive
    
    # SETTER
    @motive.setter
    def motive(self, new_value):
        self._motive = new_value