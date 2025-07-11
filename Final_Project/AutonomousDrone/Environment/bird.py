# bird
import random

class Bird:
    def __init__(self, city):
        self.city = city
        self.x, self.y = self._generate_position()
        self.city.set_bird(self.x, self.y)

    def _generate_position(self):
        possible_positions = [
            (x, y)
            for x in range(self.city.width)
            for y in range(self.city.height)
            if self.city.grid[y, x] == self.city.EMPTY
        ]
        return random.choice(possible_positions)

    def move(self):
        self.city.clear_cell(self.x, self.y)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if (0 <= new_x < self.city.width and
                0 <= new_y < self.city.height and
                self.city.grid[new_y, new_x] == self.city.EMPTY):
                self.x, self.y = new_x, new_y
                break  # only move once

        self.city.set_bird(self.x, self.y)

    @property
    def position(self):
        return (self.x, self.y)
