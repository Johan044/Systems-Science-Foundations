#drone
import random
from Environment.sensor import Sensor

class Drone:
    def __init__(self, city, energy_per_step=5):
        self.city = city
        self.energy_per_step = energy_per_step
        self.energy = 100
        self.x, self.y = self._generate_initial_position()
        self.city.set_drone(self.x, self.y)

        self.destination = self._generate_destination()
        self.city.set_destination(*self.destination)

        self.sensor = Sensor(city, self)

    def _generate_initial_position(self):
        margin = 2
        possible_positions = [
            (x, y)
            for x in range(self.city.width)
            for y in range(self.city.height)
            if (x < margin or x >= self.city.width - margin or
                y < margin or y >= self.city.height - margin) and
               self.city.grid[y, x] == self.city.EMPTY
        ]
        if not possible_positions:
            raise ValueError("There is no place for the drone.")
        return random.choice(possible_positions)

    def _generate_destination(self):
        possible_positions = [
            (x, y)
            for x in range(self.city.width)
            for y in range(self.city.height)
            if self.city.grid[y, x] == self.city.EMPTY and (x, y) != (self.x, self.y)
        ]
        return random.choice(possible_positions)

    def move(self, action):
        dx, dy = 0, 0
        if action == 0: dy = -1  # up
        elif action == 1: dy = 1   # down
        elif action == 2: dx = -1  # left
        elif action == 3: dx = 1   # right
        else:
            raise ValueError("Invalid action")

        new_x, new_y = self.x + dx, self.y + dy

        # detect collition with buildings and edges
        if not (0 <= new_x < self.city.width and 0 <= new_y < self.city.height):
            return False  # Colisión con borde
        if self.city.grid[new_y, new_x] == self.city.BUILDING:
            return False  # collition with building

        # valid action
        self.city.clear_cell(self.x, self.y)
        self.x, self.y = new_x, new_y
        self.city.set_drone(self.x, self.y)
        self.energy -= self.energy_per_step
        return True

    @property
    def position(self):
        return (self.x, self.y)

    def get_energy(self):
        return self.energy

    def get_sensor_data(self):
        return self.sensor.get_local_view()

    def estimate_energy(self, target_position):
        x1, y1 = self.position
        x2, y2 = target_position
        manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
        return manhattan_distance * self.energy_per_step
