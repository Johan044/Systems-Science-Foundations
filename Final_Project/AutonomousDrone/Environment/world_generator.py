#world_generator
import random

def generate_world(grid_size=(20, 20), building_density=0.15):
    width, height = grid_size
    total_cells = width * height
    num_buildings = int(total_cells * building_density)

    all_positions = [(x, y) for x in range(width) for y in range(height)]
    building_positions = random.sample(all_positions, num_buildings)

    return building_positions
