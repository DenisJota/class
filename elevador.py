class Elevator:
    def __init__(self, current_floor, total_floor, capacity, total_people):
        self.current_floor = current_floor
        self.total_floor = total_floor
        self.capacity = capacity
        self.total_people = total_people

    def up(self):
        if self.current_floor < self.total_floor:
            self.current_floor += 1
            print('Going UP...')
            print(f'Current floor: {self.current_floor}')
        else:
            print('You are already in the last floor!!!')

    def down(self):
        if self.current_floor > 0:
            self.current_floor -= 1
            print('Going down...')
            print(f'Current floor:{self.current_floor}')
        else:
            print('You are already in the ground floor!')

    def inside(self, x_people):
        if self.total_people + x_people <= self.capacity:
            self.total_people += x_people
            print('Getting inside...')
            print(f'Current total of people inside: {self.total_people}')
        else:
            print('Capacity not support that many people inside!')

    def out(self, x_people):
        if self.total_people - x_people >= 0:
            self.total_people -= x_people
            print('Getting Out...')
            print(f'Current total of people inside: {self.total_people}')
        else:
            print('There is not negative people!')


plaza = Elevator(2, 10, 5, 3)
rio_mar = Elevator(3, 3, 6, 4)

print(f"Full capacity in plaza elevator: {plaza.capacity}")
plaza.up()
plaza.down()
plaza.inside(5)
plaza.out(1)