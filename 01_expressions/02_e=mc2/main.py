"""
Program: Mass-Energy Equivalence Calculator
------------------------------------------
This program calculates the energy equivalent of a given mass using Einstein's formula E = m * c^2.
"""

# Speed of light in meters per second (constant)
C = 299792458

def main():
    # Prompt the user to enter the mass in kilograms
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate the energy using Einstein's formula: E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the calculation and result
    print("e = m * C^2...")
    print("m =", mass_in_kg, "kg")
    print("C =", C, "m/s")
    print(energy_in_joules, "joules of energy!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()