class Ones_threes_nines:
    def __init__(self,num:float):
        self.__num = num
        self.ones = num
        self.threes = int(num / 3)
        self.nines = int(num / 9)

