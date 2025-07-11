#drone env
from Environment.city import City
from Environment.drone import Drone
from Environment.bird import Bird

class DroneEnv:
    def __init__(self, enable_render=True):
        self.city = City(enable_render=enable_render)
        self.drone = Drone(self.city)
        self.bird = Bird(self.city)
        self.done = False
        self.total_reward = 0

    def reset(self):
        self.__init__(enable_render=self.city.enable_render)
        return self.get_observation()

    def get_observation(self):
        return {
            "sensor_view": self.drone.get_sensor_data(),
            "position": self.drone.position,
            "energy": self.drone.get_energy(),
            "estimated_energy": (self.drone.estimate_energy(self.city.delivery_point), self.city.delivery_point),
            "bird_position": self.bird.position,
        }

    def step(self, action):
        if self.done:
            return self.get_observation(), 0, True

        self.bird.move()
        moved = self.drone.move(action)
        new_pos = self.drone.position

        reward = -1

        if not moved:
            reward = -50
            self.done = True
        elif new_pos == self.bird.position:
            reward = -50
            self.done = True
        elif new_pos == self.city.delivery_point:
            reward = 100
            self.done = True

        self.total_reward += reward
        obs = self.get_observation()
        return obs, reward, self.done

    def render(self):
        self.city.render(self.drone.position)
