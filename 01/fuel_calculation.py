import numpy as np


def fuel_for_mass(mass, task=1):
    assert task in [1, 2], f"Invalid task number {task}. Valid options are '1', '2'."
    if task == 1:
        return int(np.floor(mass/3)-2)
    elif task == 2:
        fuel = int(np.floor(mass/3)-2)
        if np.floor(fuel/3)-2 > 0:
            fuel += fuel_for_mass(fuel, task=2)
        return fuel


def get_module_masses(f_mass):
    with open(f_mass, 'r') as f:
        raw_lines = f.readlines()
    return [int(m.rstrip('\n')) for m in raw_lines]


def get_launch_fuel(f_mass, task=1):
    masses = get_module_masses(f_mass)
    fuel_list = [fuel_for_mass(m, task) for m in masses]
    fuel = sum(int(f) for f in fuel_list)

    return fuel


input_file = 'D:\\Code\\Advent of Code 2019\\01\\input'
required_fuel = get_launch_fuel(input_file, task=2)

print(f"Required fuel: {required_fuel}")
