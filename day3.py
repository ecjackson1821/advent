# Advent of Code Day 3
import numpy as np

diagnostics = [i for i in open('day3_input.txt').read().split()]

def binary_diagnostic(diagnostics):
    """
    Calculates the gamma and epsilon rate from a a list of
    binary numbers which make up the submarine's diagnostic report

    Inputs:
        diagnostics: list of binary numbers 

    Returns the product of the gamma and epsilon rate
    """
    bin_len = len(diagnostics[0])
    gamma = ""
    epsilon = ""
    for x in range(bin_len):
        pos_list = []
        for bin in diagnostics:
            pos_list.append(bin[x])
        gamma_val = np.bincount(pos_list).argmax()
        epsilon_val = np.bincount(pos_list).argmin()
        gamma = gamma + str(gamma_val)
        epsilon = epsilon + str(epsilon_val)
    print(gamma)
    print(epsilon)
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    return gamma * epsilon

            



