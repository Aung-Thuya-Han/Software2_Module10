class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = 0

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            if self.current_floor == self.bottom:
                print("Elevator is now at Ground Floor.")
            else:
                print(f"Elevator is now at floor {self.current_floor}")


    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

elevator = Elevator(0, 5)
elevator.go_to_floor(5)
elevator.go_to_floor(0)
