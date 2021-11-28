# Name: Kody McLeod
# ID: 001133999

from algorithm import delivery_system, print_total_miles
from packages import package_lookup

# The starting main menu with options.
class main:

    # Initializes menu = 0.
    menu = 0

    # Calls the function that calculates total miles driven when the main menu is opened.
    print_total_miles()

    # Lists the menu options.
    while menu != 3:
        print("""
 Choose one of the following options (Type 1, 2, or 3):
 1. Search for a package
 2. Enter a time and display package status
 3. Exit the program
			""")
        menu = int(input())

        # Takes user to general package information at start of day.
        if menu == 1:
            package_lookup()

        # Takes user to package tracking.
        elif menu == 2:
            delivery_system()


