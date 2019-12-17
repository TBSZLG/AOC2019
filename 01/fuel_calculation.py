import numpy as np


def fuel_for_mass(mass):
    return int(np.floor(int(mass)/3)-2)


def get_module_masses(f_mass):
    with open(f_mass, 'r') as f:
        raw_lines = f.readlines()
    return [m.rstrip('\n') for m in raw_lines]


def get_launch_fuel(f_mass):
    masses = get_module_masses(f_mass)
    fuel_list = [fuel_for_mass(m) for m in masses]
    fuel = sum(int(f) for f in fuel_list)

    return fuel


input_file = 'D:\\Code\\Advent of Code 2019\\01\\input'
required_fuel = get_launch_fuel(input_file)

print(f"Required fuel: {required_fuel}")
