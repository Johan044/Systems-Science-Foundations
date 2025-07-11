#sensor

class Sensor:
    def __init__(self, city, drone, view_range=2):
        self.city = city
        self.drone = drone
        self.view_range = view_range  # sensor 5x5 → range = 2

    def get_view(self, grid, position):
        x, y = position
        size = self.view_range
        view = []

        for dy in range(-size, size + 1):
            row = []
            for dx in range(-size, size + 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.city.width and 0 <= ny < self.city.height:
                    row.append(grid[ny, nx])
                else:
                    row.append(-1)  # value for things ouside the grid
            view.append(row)

        return view

    def get_local_view(self):
        return self.get_view(self.city.grid, self.drone.position)
