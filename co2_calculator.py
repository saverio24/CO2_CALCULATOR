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
