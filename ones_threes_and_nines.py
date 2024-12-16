class ones_three_nines:
    def __init__(self,num:float):
        self.__num = num
        self.__ones = num
        self.__threes = int(num / 3)
        self.__nines = int(num / 9)
    
    def ones(self):
        return self.__ones
    
    def threes(self):
        return self.__threes
    
    def nines(self):
        return self.__nines
