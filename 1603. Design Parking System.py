class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_capacity = big
        self.cur_big_capacity = 0

        self.medium_capacity = medium
        self.cur_medium_capacity = 0

        self.small_capacity = small
        self.cur_small_capacity = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.cur_big_capacity < self.big_capacity:
                self.cur_big_capacity += 1
                return True
            else:
                return False

        elif carType == 2:
            if self.cur_medium_capacity < self.medium_capacity:
                self.cur_medium_capacity += 1
                return True
            else:
                return False

        elif carType == 3:
            if self.cur_small_capacity < self.small_capacity:
                self.cur_small_capacity += 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)