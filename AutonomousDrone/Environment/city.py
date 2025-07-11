#city
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from Environment.world_generator import generate_world

class City:
    def __init__(self, width=20, height=20, enable_render=True):
        self.width = width
        self.height = height
        self.enable_render = enable_render

        self.EMPTY = 0
        self.BUILDING = 1
        self.DRONE = 2
        self.DESTINATION = 3
        self.BIRD = 4

        self.grid = np.zeros((height, width), dtype=int)
        building_coords = generate_world(grid_size=(width, height))
        for (x, y) in building_coords:
            self.add_building(x, y)

        self.delivery_point = None

        if self.enable_render:
            self.fig, self.ax = plt.subplots(figsize=(8, 8))
            plt.ion()
            plt.show(block=False)
            self._setup_plot()
        else:
            self.fig, self.ax = None, None

    def _setup_plot(self):
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_xticks(np.arange(0, self.width + 1, 1))
        self.ax.set_yticks(np.arange(0, self.height + 1, 1))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_aspect("equal")
        self.ax.grid(True, which="both", color="lightgray", linewidth=0.5)

        legend_patches = [
            mpatches.Patch(color="white", label="Empty"),
            mpatches.Patch(color="black", label="Building"),
            mpatches.Patch(color="green", label="Drone"),
            mpatches.Patch(color="red", label="Delivery point"),
            mpatches.Patch(color="blue", label="Bird")
        ]
        self.ax.legend(
            handles=legend_patches,
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            borderaxespad=1,
            title="Conventions"
        )
        plt.subplots_adjust(right=0.75)

    def add_building(self, x, y):
        self.grid[y, x] = self.BUILDING

    def set_drone(self, x, y):
        self.grid[y, x] = self.DRONE

    def set_destination(self, x, y):
        self.delivery_point = (x, y)
        self.grid[y, x] = self.DESTINATION

    def set_bird(self, x, y):
        self.grid[y, x] = self.BIRD

    def clear_cell(self, x, y):
        self.grid[y, x] = self.EMPTY

    def render(self, drone_pos=None):
        if not self.enable_render:
            return

        self.ax.clear()
        self._setup_plot()

        cmap = {
            self.EMPTY: "white",
            self.BUILDING: "black",
            self.DRONE: "green",
            self.DESTINATION: "red",
            self.BIRD: "blue"
        }

        for y in range(self.height):
            for x in range(self.width):
                color = cmap[self.grid[y, x]]
                rect = plt.Rectangle((x, self.height - y - 1), 1, 1, facecolor=color, edgecolor="lightgray")
                self.ax.add_patch(rect)

        if drone_pos:
            dx, dy = drone_pos
            for dy_offset in range(-2, 3):
                for dx_offset in range(-2, 3):
                    nx, ny = dx + dx_offset, dy + dy_offset
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        outline = plt.Rectangle((nx, self.height - ny - 1), 1, 1, fill=False, edgecolor="orange", linewidth=2)
                        self.ax.add_patch(outline)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.01)
