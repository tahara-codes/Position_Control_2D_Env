import time
import numpy as np

import gym
import position_control_2d_env


class Test_PositionControl2D:
    def __init__(self):
        np.set_printoptions(precision=3, suppress=True)
        self.envname = "position_control_2d-v0"
        self.env = gym.make(self.envname)

    def main(self):
        s = self.env.reset()
        while True:
            a = np.array([0.1, 0.0])
            s, r, goal, death = self.env.step(a)
            self.env.render("human")
            print(s, a, r, goal, death)
            time.sleep(1)


if __name__ == "__main__":
    test_env = Test_PositionControl2D()
    test_env.main()
