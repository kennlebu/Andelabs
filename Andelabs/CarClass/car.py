class Car:
    def __init__(self, name='General', model='GM', type='saloon'):
        self.name = name
        self.model = model
        self.type = type
        self.num_of_doors = 0
        self.num_of_wheels = 0
        self.speed = 0
        self.parked_speed = 0
        self.moving_speed = 0

        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            self.num_of_doors = 2
        else: self.num_of_doors = 4

        if self.type == 'trailer':
            self.num_of_wheels = 8
        else: self.num_of_wheels = 4

    def is_saloon(self):
        if self.type == 'saloon': return True
        return False

    def drive(self, top_speed):
        if self.type == 'saloon':
            self.moving_speed = 10**top_speed
            self.speed = self.moving_speed
            return self
        else:
            self.moving_speed = 11*top_speed
            self.speed = self.moving_speed
            return self
            
            
