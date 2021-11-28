import csv
from addresses import find_ID_by_address

# The nested dictionary data type was utilized for storing all package information.
package_id = {}

# This function prints details for packages
# O(1)
def package_dict(pid):
    print("Package ID:", pid)
    print('Address:', combine_full_address((pid)))
    print('Delivery Deadline:',
          package_id[pid].get('delivery_deadline'))
    print('Weight:', package_id[pid].get('weight'), 'lb(s)')
    print('Special Information:',
          package_id[pid].get('package_rules'))
    print('Truck Assignment:', package_id[pid].get('truck'))
    return print('Delivery Status:', package_id[pid].get('delivery_status'))


# Function puts the full address into a single string.
# O(1)
def combine_full_address(searched_id):
    id = str(searched_id)
    address = package_id[id].get('address')
    city = package_id[id].get('city')
    state = package_id[id].get('state')
    zip_code = package_id[id].get('zip_code')
    full_address = address + ', ' + city + ', ' + state + " " + zip_code
    return full_address


# Function counts the total packages in a truck.
# O(N)
def total_inTruck(truck_number):
    count = 0
    for id in package_id:
        if package_id[id]['truck'] == truck_number:
            count = count + 1
    return count


with open('data/WGUPS Package File.csv', mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        # This process opens the CSV package file.
        # Assigns all the package details to a dict.
        # O(N)
        package_id[row[0]] = {'address': row[1], 'city': row[2], 'state': row[3],
                              'zip_code': row[4], 'delivery_deadline': row[5],
                              'weight': row[6], 'package_rules': row[7],
                              'delivery_status': 'At Hub', 'truck': 'Not Assigned',
                              'delivery_start': '1', 'delivery_end': 'Not Assigned', 'delivered_time': 'Undelivered'
                              }
    for id in package_id:
        # Assigns each package to a truck 1,2 or 3 based on rules.
        # O(N)
        if 'Wrong address' in package_id[id]['package_rules']:
            package_id[id]['truck'] = 3
            package_id[id]['address'] = '410 S State St'
            package_id[id]['zip_code'] = '84111'
        if 'Can only' in package_id[id]['package_rules']:
            package_id[id]['truck'] = 2
        if 'Delayed' in package_id[id]['package_rules']:
            package_id[id]['truck'] = 2
        if package_id[id]['delivery_deadline'] != 'EOD':
            package_id[id]['truck'] = 1
        if package_id[id]['truck'] == 'Not Assigned':
            # Assigns any non-special rules packages between trucks 1, 2, and 3.
            if total_inTruck(1) < 16:
                package_id[id]['truck'] = 1
            elif total_inTruck(2) < 16:
                package_id[id]['truck'] = 2
            elif total_inTruck(3) < 16:
                package_id[id]['truck'] = 3

    truck1 = []
    truck2 = []
    truck3 = []

    # Creates a list of packages in each truck.
    # O(N)
    for id in package_id:
        if package_id[id]['truck'] == 1:
            add_to_truck = int(id)
            truck1.append(add_to_truck)
        if package_id[id]['truck'] == 2:
            add_to_truck = int(id)
            truck2.append(add_to_truck)
        if package_id[id]['truck'] == 3:
            add_to_truck = int(id)
            truck3.append(add_to_truck)


# Function takes the delivery address of a package.
# Matches that address to a location ID.
# O(1)
def get_deliveryID(test_package_id):
    package_id_string = str(test_package_id)
    package_delivery_address = package_id[package_id_string]['address']
    return find_ID_by_address(package_delivery_address)


# Function used to check the status of a package at the start of the day.
# O(1)
def package_lookup():
    max = len(package_id) + 1
    user_input = int(input('Enter a package ID: '))
    if user_input in range(1, max):
        user_input = str(user_input)
        package_dict(user_input)
    elif user_input not in range(1, max):
        print('Invalid Entry')


# Function to print the data required.
# O(N)
def print_formatted():
    for index in package_id:
        print("Package ID:", index, "| Address:", combine_full_address(index), "| Deadline:",
              package_id[index]['delivery_deadline'], '| Package Weight:', package_id[index]['weight'],
              '| Delivery Status:', package_id[index]['delivery_status'], '| Time Delivered:',
              package_id[index]['delivered_time'])
