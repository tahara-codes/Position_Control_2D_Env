import pygame
from pygame.locals import *
import time


def main():
    controller = JoyController()

    while True:
        controller.get_controller_value()

        print(
            "X(L)- ",
            controller.l_hand_x,
            "Y(L)- ",
            controller.l_hand_y,
            "X(R)- ",
            controller.r_hand_x,
            "Y(R)- ",
            controller.r_hand_y,
            "Up- ",
            controller.hand_up,
        )

        if controller.exit_b:
            print("EXIT")
            break

        time.sleep(0.1)


class JoyController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        self.weight_coff = 0.1

        self.l_hand_x = 0.0
        self.l_hand_y = 0.0
        self.r_hand_x = 0.0
        self.r_hand_y = 0.0
        self.hand_up = 0.0
        self.exit_b = False
        self.start_b = False

        self.__initialize_controller()

    def __initialize_controller(self):
        self.joys = pygame.joystick.Joystick(0)
        self.joys.init()

        self.initialize_updown()

    def initialize_updown(self):
        print('Please Push "LT" and "RT"')

        while self.joys.get_axis(2) == 0.0 or self.joys.get_axis(5) == 0.0:
            _ = pygame.event.get()
            time.sleep(0.1)

    def reload_checker(self):
        print('Please Push "START" button')

        while not self.start_b:
            self.get_controller_value()

        self.start_b = False

    def get_controller_value(self):
        for eventlist in pygame.event.get():
            if eventlist.type == JOYAXISMOTION:
                self.l_hand_x = round(
                    -self.joys.get_axis(0) * self.weight_coff, 2
                )  # joy_left(left_hand [L<->R])
                self.l_hand_y = round(
                    -self.joys.get_axis(1) * self.weight_coff, 2
                )  # joy_left(left_hand [U<->D])
                self.r_hand_x = round(
                    -self.joys.get_axis(3) * self.weight_coff, 2
                )  # joy_right(left_hand [L<->R])
                self.r_hand_y = round(
                    -self.joys.get_axis(4) * self.weight_coff, 2
                )  # joy_right(left_hand [U<->D])
                up = (self.joys.get_axis(2) + 1) / 2.0 * self.weight_coff  # LT key
                down = -(self.joys.get_axis(5) + 1) / 2.0 * self.weight_coff  # RT key

                if up != 0.0:
                    self.hand_up = up
                else:
                    self.hand_up = down

            if eventlist.type == JOYBUTTONDOWN:
                self.exit_b = self.joys.get_button(8)
                self.start_b = self.joys.get_button(7)


if __name__ == "__main__":
    main()
