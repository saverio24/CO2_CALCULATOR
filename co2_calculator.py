# --- CO₂ Calculator Program ---
# This script estimates a user's annual carbon footprint based on lifestyle data.

import matplotlib.pyplot as plt

def calculate_co2():
    """
    Calculate and display a user's estimated annual CO2 footprint.

    This function collects lifestyle data from the user (transportation habits,
    electricity usage, and meat consumption), applies standard CO2 emission
    factors, and computes annual emissions for each category. It prints the
    numerical results, provides simple feedback based on the user's total
    emissions, and generates a bar chart visualizing :emissions by category.

    The function performs the following steps:
    1. Prompt the user for weekly or monthly activity data.
    2. Convert the input into annual CO2 emissions using predefined emission factors.
    3. Organize results into a dictionary for display and plotting.
    4. Print detailed results and an overall yearly footprint.:
    5. Display a bar chart using matplotlib to visualize emissions.

    No arguments are required, and no values are returned.
    All results are displayed directly to the user.
    """
    print("🌍 Personal CO₂ Footprint Calculator\n")
# --- User input ---
    km_car: float = float(input("How many km do you drive by car per week? "))
    km_bus: float = float(input("How many km do you travel by bus per week? "))

    # Short-haul flights
    print("\n✈ SHORT-HAUL FLIGHTS:")
    print("Short-haul flights are usually under 3 hours, roughly less than 1500–2000 km.")
    print("Examples: Rome → Madrid, Paris → London.")
    short_flights: int = int(input("How many short-haul flights did you take this year? "))

    # Long-haul flights
    print("\n✈ LONG-HAUL FLIGHTS:")
    print("Long-haul flights usually last more than 3 hours and often cross continents.")
    print("Examples: Rome → New York, Madrid → Buenos Aires.")
    long_flights: int = int(input("How many long-haul flights did you take this year? "))

    # Electricity consumption
    electricity_use: float = float(input("\nMonthly electricity consumption (in kWh): "))

    meat_meals: int = int(input("How many meals with meat do you eat per week? "))

