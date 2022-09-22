import numpy as np
from matplotlib import pyplot as plt
#(b - a) * random_sample() + a

'''def rand_h(minh, maxh):
    # 
    diff = maxh - minh
    selected = np.random.random_sample(minh, maxh, 1)
    height = minh + diff*selected
    return height'''


def partition(h, k=1, g=1, m=1, T=1):
    Z = np.exp((m * g * h) / (k * T))
    return Z


heights = []


def monte_carlo(samples=100):
    '''lower = 0
    upper = 1'''

    density = 0
    for s in range(samples):
        h = round(np.random.random_sample(), 1)
        heights.append(h)
        density += partition(h)
    return heights


plt.hist(heights, 10)


def proph(current_Height, scale):
    # draw a jump from some dist
    # uniform dist centered on zero and from -scale/2 to +scale/2
    jump = scale * (np.random.rand() - 0.5)
    return current_Height + jump


def accerpt_MCmove(previous_Height, proposed_Height, delta_Energy, T):
    '''
    Returns true if we accept the move, fale if we don't
    '''
    height_greaterThanZero = proposed_Height > 0
    height_below = proposed_Height < previous_Height
    acceptProbability = np.exp(-deltaEnergy / T)

    accept = height_greaterThanZero and (heightBelow or (acceptProbability > np.random.rand()))
    return accept


def calc_Energy(height, mass, g):
    return mass * g * height


def monteCarloSim(numsteps, mass=1, g=1, T=1):
    '''
    Run a monte carlo sim of a single particle of mass in a
    gravitational well with acceleration g at temperature T.
    We will start at some initial height and propose a new height
    from some random dist.
    If the energy associated with the new height is smaller, then
    we move to that height. If the energy is larger, then we move
    to that height with prob e^-deltaE/T
    No heights are accepted that bring the system below zero.

    args:
        numsteps(int): the number of monte carlo steps to execute
        mass(float): the mass
        g(float): acceleration due to gravity
        T(float): temperature

    return:
        heights(list of floats): the height at every MC step
    '''

    # set the initial height
    heights = [0]
    # compute the scale for proposed jumps drawn from a random dist.
    scale = T / (mass * g)
    # start monte carlo loop
    for i in range(numsteps):
        proposed_newHeight = propose_Height(heights[-1], scale)
        proposed_Energy = calc_Energy(proposed_newHeight, mass, g)
        previous_Energy = calc_Energy(heights[-1], mass, g)
        delta_Energy = proposed_Energy - previous_Energy
        if accerpt_MCmove(previous_Height propose_Height, delta_Energy, T):
            heights.append(proposed_newHeight)
        else:
            heights.append(heights[-1])


heights = monteCarloSim(10)
# heights = monteCarloSim(10, T = 10, mass = 100, g = 1e-10)
# varying temperature and mass, smaller g going farther out into space
plt.plot(heights)
plt.figure(2)
plt.hist(heights)
#plt.hist(heights, density = 'true'), showing prob density
plt.yscale('log')
x = np.arrange(10)
h0 = 1
plt.plot(h.np.exp(-h/h0))