#!/usr/bin/env python3

import time
import numpy as np
import gym
from gym import wrappers
import position_control_2d_env
import pygame
from matplotlib import pyplot as plt
from control_joy import JoyController


class Test_PositionControl2D:
    def __init__(self):
        np.set_printoptions(precision=3, suppress=True)

        # env
        self.envname = "position_control_2d-v0"
        self.env = gym.make(self.envname)
        self.env.reset()

        # controller
        self.joy = JoyController()
        self.deadzone = 0.01

    # Gamepad input
    def human_controller(self):
        self.joy.get_controller_value()
        y = self.joy.l_hand_y
        x = -self.joy.l_hand_x
        action = [x, y]
        return np.array(action)

    def main(self):

        self.env.reset()

        while True:
            self.env.render("human")
            a = self.human_controller()
            s, r, goal, death = self.env.step(a)
            print(s, a, r, goal, death)
            time.sleep(0.1)


if __name__ == "__main__":
    test_env = Test_PositionControl2D()
    test_env.main()
