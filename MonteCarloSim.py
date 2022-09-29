from numpy import *
from matplotlib import pyplot as plt


class MC:
    def __init__(self, k=1, g=1, m=1, T=1):
        '''
        :param k: constant
        :param g: acceleration due to gravity
        :param m: mass
        :param T: temperature
        '''
        self.k = k
        self.g = g
        self.m = m
        self.T = T

    def partition(self, h):
        Z = exp((self.m * self.g * h) / (self.k * self.T))
        return Z

    def prop_h(self, current_height: float, scale: float):
        '''
        draw a jump from some dist
        uniform dist centered on zero and from -scale/2 to +scale/2
        '''
        jump = scale * (random.rand() - 0.5)
        return current_height + jump

    def test_move(self, previous_height, proposed_height, delta_energy) -> bool:
        '''
        :param previous_height:
        :param proposed_height:
        :param delta_energy:

        :return:
            True if move accepted, False if move denied
        '''
        height_status = proposed_height > 0
        height_below = proposed_height < previous_height
        probability = exp(-delta_energy / self.T)
        return height_status and (height_below or (probability > random.rand()))

    def energy(self, height: float) -> float:
        return self.m * self.g * height

    def sim(self, num_steps: int) -> list[float]:
        '''
        A Monte Carlo Simulation of a single particle of mass m in a gravitational well
        with acceleration g at temperature T. Start at some initial height and propose a
        new height from some random distance. If the energy associated with the
        new height is smaller, then we move to that height. If the energy is larger, then
        we move to that height with prob e^-deltaE/T. No heights are accepted that bring
        the system below zero.

        :param num_steps: number of Monte Carlo steps to execute
        :return: heights: list of height at every MC step
        '''
        heights = [0]   # set the initial height
        scale = self.T / (self.m * self.g)   # compute the scale for proposed jumps
        for i in range(num_steps):
            h = self.prop_h(heights[-1], scale)
            prop_E = self.energy(h)
            prev_E = self.energy(heights[-1])
            delta_energy = prop_E - prev_E
            if self.test_move(heights[-1], h, delta_energy):
                heights.append(h)
            else:
                heights.append(heights[-1])
        return heights

    def display(self, heights: list[float]):
        # heights = sim(10, T = 10, mass = 100, g = 1e-10)
        # varying temperature and mass, smaller g going farther out into space
        plt.plot(heights)
        plt.figure(2)
        plt.hist(heights)
        # plt.hist(heights, density = 'true'), showing prob density
        plt.yscale('log')
        x = arrange(10)
        h0 = 1
        plt.plot(h.exp(-h/h0))


def main():
    mc = MC()
    mc.display(mc.sim(10))


if __name__ == "__main__":
    main()