# Constant: speed of light in meters per second
C: int = 299792458  # m/s

def main():
    # Ask the user to enter mass in kilograms
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's formula
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Show step-by-step calculation to the user
    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!\n")

# This is the standard Python entry point
if __name__ == '__main__':
    main()
