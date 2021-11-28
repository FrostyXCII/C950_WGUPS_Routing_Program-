import csv

# I used a nested dictionary data type for WGUPS Distance Table.csv.
addresses = {}

# O(N)
with open('data/WGUPS Distance Table.csv', mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        addresses[row[0]] = {'location_id': row[0], 'location_name': row[1],
                         'location_address': row[2], '1': row[3], '2': row[4], '3': row[5],
                         '4': row[6], '5': row[7], '6': row[8], '7': row[9], '8': row[10],
                         '9': row[11], '10': row[12], '11': row[13], '12': row[14],
                         '13': row[15], '14': row[16], '15': row[17], '16': row[18],
                         '17': row[19], '18': row[20], '19': row[21], '20': row[22],
                         '21': row[23], '22': row[24], '23': row[25], '24': row[26],
                         '25': row[27], '26': row[28], '27': row[29]}


# Function to find the distance between two locations.
# O(1)
def find_distance(start, end):
    distance = float(addresses[start][end])
    return distance


# Function used to find the ID of the location by inputting the address.
# O(N)
def find_ID_by_address(package_address):
    for row in addresses:
        if addresses[row]['location_address'] == package_address:
            delivery_id = addresses[row]['location_id']
            return delivery_id
