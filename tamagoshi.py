class Tamagochi:
    def __init__(self, name, hungry, energy):
        self.name = name
        self.hungry = hungry
        self.energy = energy

    def eat(self):
        if self.hungry + 10 <= 100:
            self.hungry += 10
            print(f'Eating...'
                  f'he is feed by {self.hungry}%')
        else:
            print(f'Its not hungry right now...')

    def sleep(self):
        if self.energy + 15 <= 100:
            self.energy += 15
            print(f'Sleeping...'
                  f'His energy are full by {self.energy}%')
        else:
            print(f'Its not tired right now...')

    def status(self):
        print(f'Name of your tamagochi: {self.name}'
              f'he is feed by {self.hungry}%'
              f'His energy are full by {self.energy}%')

    def time(self):
        self.energy -= 15
        self.hungry -= 20
        print(f'Time goes by and your tamagochi ares tired and hungry again'
              f'\nenergy level: {self.energy}%'
              f'\nfood level: {self.hungry}')


tommy = Tamagochi('Tommy', 50, 50)
tommy.sleep()
tommy.eat()
tommy.status()