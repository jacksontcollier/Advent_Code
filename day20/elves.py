#!/usr/bin/env python3

def first_house_with_num_presents(num_presents, chunk, max_presents_per_elf,
                                  present_multiplication_factor):

    while True:
        house_presents = first_n_house_presents(chunk, max_presents_per_elf,
                                                present_multiplication_factor)
        current_elf_presents = 0
        for house, presents in enumerate(house_presents):
            if presents >= num_presents:
                return house

            current_elf_presents += 1

        chunk *= 2

def first_n_house_presents(first_n_houses, max_presents_per_elf,
                           present_multiplication_factor):
    house_presents = [0]

    for house in range(first_n_houses):
        house_presents.append(0)

    for elf in range(1, first_n_houses + 1):
        house = elf
        while house <= first_n_houses:
            if (max_presents_per_elf != None
                    and house / elf > max_presents_per_elf):
                break
            house_presents[house] += elf * present_multiplication_factor
            house += elf

    return house_presents


