class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self, carType: int) -> bool:
        if self.big<0:
            self.big=0
        elif self.medium<0:
            self.medium=0
        elif self.small<0:
            self.small=0
        if carType==1:
            self.big-=1
        elif carType==2:
            self.medium-=1
        else:
            self.small-=1
        return self.big>=0 and self.medium>=0 and self.small>=0
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)