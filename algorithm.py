from datetime import timedelta
from addresses import find_distance
from packages import get_deliveryID, truck1, truck2, truck3, package_id, print_formatted


# Uses the Greedy Algorithm.
# Starts with the first package in the list and finds the next closest location among the remaining packages.
# O(N^2)
def sort_trucks(truck_list):
    list = truck_list[:]
    optimized_truck = []
    max = len(list)
    current_location = '1'
    total_miles = 0

    # 1st for loops initializes values to be adjusted by the 2nd for loop.
    for i in range(0, max):
        min = 100.0
        package = 41
        next_location = '0'
        index = 0

        # 2nd for loop finds the shortest distance and updates values in the 1st loop accordingly.
        for j in range(0, len(list)):

            # Checks for the final value and sends it back to WGUPS.
            if len(list) == 1:
                next_location = '1'
                min = find_distance(current_location, next_location)
                index = j
                package = list[j]
                break

            # If distance is shortest, updates min distance values.
            search_packageID = int(list[j])
            test = get_deliveryID(search_packageID)
            if find_distance(current_location, test) <= min:
                min = find_distance(current_location, test)
                next_location = test
                index = j
                package = list[j]

        package_id[str(package)]['delivery_start'] = current_location
        package_id[str(package)]['delivery_end'] = next_location
        optimized_truck.append(list[index])
        list.pop(index)
        current_location = next_location
        total_miles = total_miles + min
    return optimized_truck, total_miles


# Returns the truck list with packages organized based on delivery and
# the total miles for delivery and return to hub as well as creates a starting time for
# each truck so no more than two are on the road simultaneously.
# O(N^2)
def delivery_system():
    truck1_sorted_list, total_miles_truck1 = sort_trucks(truck1)
    truck2_sorted_list, total_miles_truck2 = sort_trucks(truck2)
    truck3_sorted_list, total_miles_truck3 = sort_trucks(truck3)
    truck1_start = timedelta(hours=8, minutes=0, seconds=0)
    truck2_start = timedelta(hours=9, minutes=5, seconds=0)
    truck3_start = timedelta(hours=10, minutes=0, seconds=0)
    user_time = input('Please enter a time in the HH:MM:SS format: ')
    (h, m, s) = user_time.split(':')
    convert_time = timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    # Truck 1 packages are delivered until the time specified by the user.
    if truck1_start <= convert_time:
        list = truck1_sorted_list[:]
        delivering(truck1_sorted_list)
        while truck1_start <= convert_time and len(list) != 0:
            for index in truck1_sorted_list:
                minutes = timedelta(minutes=check_distance_time(index)*60)
                if truck1_start + minutes <= convert_time:
                    truck1_start = truck1_start + minutes
                    delivered(index, truck1_start)
                    list.remove(index)
                else:
                    truck1_start = truck1_start + minutes
                    list.remove(index)

    # Truck 2 packages are delivered until the time specified by the user.
    if truck2_start <= convert_time:
        list2 = truck2_sorted_list[:]
        delivering(truck2_sorted_list)
        while truck2_start <= convert_time and len(list2) != 0:
            for index in truck2_sorted_list:
                minutes = timedelta(minutes=check_distance_time(index)*60)
                if truck2_start + minutes <= convert_time:
                    truck2_start = truck2_start + minutes
                    delivered(index, truck2_start)
                    list2.remove(index)
                else:
                    truck2_start = truck2_start + minutes
                    list2.remove(index)

    # Truck 3 packages are delivered until the time specified by the user.
    if truck3_start <= convert_time:
        list3 = truck3_sorted_list[:]
        delivering(truck3_sorted_list)
        while truck3_start <= convert_time and len(list3) != 0:
            for index in truck3_sorted_list:
                minutes = timedelta(minutes=check_distance_time(index)*60)
                if truck3_start + minutes <= convert_time:
                    truck3_start = truck3_start + minutes
                    delivered(index, truck3_start)
                    list3.remove(index)
                else:
                    truck3_start = truck3_start + minutes
                    list3.remove(index)

    print_formatted()

# Updates packages delivery status to delivered and the time delivered.
# O(1)
def delivered(pid_list, time_delivered):
    package_id[str(pid_list)]['delivery_status'] = 'Delivered'
    package_id[str(pid_list)]['delivered_time'] = time_delivered

# Updates packages delivery status to Out for Delivery.
# O(N)
def delivering(p_list):
    for index in p_list:
        package_id[str(index)]['delivery_status'] = 'En Route'

# Checks travel time to go from one point to another.
# O(1)
def check_distance_time(id):
    delivery_start_id = package_id[str(id)]['delivery_start']
    delivery_end_id = package_id[str(id)]['delivery_end']
    distance = find_distance(delivery_start_id, delivery_end_id)
    time_adjust = distance / 18
    return(time_adjust)

# Function to print the total miles the trucks traveled.
# O(1)
def print_total_miles():
    truck1_sorted_list, total_miles_truck1 = sort_trucks(truck1)
    truck2_sorted_list, total_miles_truck2 = sort_trucks(truck2)
    truck3_sorted_list, total_miles_truck3 = sort_trucks(truck3)
    all_trucks_total = total_miles_truck1 + total_miles_truck2 + total_miles_truck3
    print('Total miles to deliver packages:', all_trucks_total)