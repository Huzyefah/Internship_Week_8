# Constants
BOAT_COST_HOUR = 20
BOAT_COST_HALF_HOUR = 12
OPENING_TIME = 10
CLOSING_TIME = 17
NUM_BOATS = 10

# Data structure to store information for each boat
boats = [{'hours_hired': 0, 'return_time': 0} for _ in range(NUM_BOATS)]

# Task 1 – Calculate the money taken in a day for one boat
def calculate_daily_profit_one_boat(boat_num):
    try:
        current_time = float(input("Enter the current time (in 24-hour format): "))

        if current_time < OPENING_TIME or current_time > CLOSING_TIME:
            print("Error: Boats can only be hired between 10:00 and 17:00.")
            return

        duration = float(input("Enter the duration of hire (in hours): "))

        if duration <= 0:
            print("Error: Invalid duration. Duration must be greater than zero.")
            return

        if current_time + duration > CLOSING_TIME:
            print("Error: Boat must be returned before 17:00.")
            return

        if current_time < OPENING_TIME:
            current_time = OPENING_TIME

        if duration >= 1:
            cost = BOAT_COST_HOUR * duration
        else:
            cost = BOAT_COST_HALF_HOUR

        boats[boat_num - 1]['hours_hired'] += duration
        boats[boat_num - 1]['return_time'] = current_time + duration

        print(f"Boat {boat_num} hired for {duration} hours. Cost: ${cost:.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numerical values.")

# Task 2 – Find the next boat available
def find_next_available_boat():
    current_time = float(input("Enter the current time (in 24-hour format): "))
    available_boats = []

    for i in range(NUM_BOATS):
        if current_time >= boats[i]['return_time']:
            available_boats.append(i + 1)

    if not available_boats:
        next_available_time = min(boats, key=lambda x: x['return_time'])['return_time']
        print(f"No boats available. Next available time: {next_available_time}")
    else:
        print(f"Available boats: {available_boats}")

# Task 3 – Calculate the money taken for all the boats at the end of the day
def calculate_daily_profit_all_boats():
    total_money_taken = 0
    total_hours_hired = 0
    unused_boats = []
    max_hours_hired = 0
    busiest_boat = 0

    for i in range(NUM_BOATS):
        total_money_taken += boats[i]['hours_hired'] * BOAT_COST_HOUR
        total_hours_hired += boats[i]['hours_hired']

        if boats[i]['hours_hired'] == 0:
            unused_boats.append(i + 1)

        if boats[i]['hours_hired'] > max_hours_hired:
            max_hours_hired = boats[i]['hours_hired']
            busiest_boat = i + 1

    print(f"Total money taken for all boats: ${total_money_taken:.2f}")
    print(f"Total hours boats were hired: {total_hours_hired} hours")
    print(f"Boats not used today: {unused_boats}")
    print(f"Boat {busiest_boat} was used the most with {max_hours_hired} hours.")

# Test the program
for boat_number in range(1, NUM_BOATS + 1):
    calculate_daily_profit_one_boat(boat_number)

find_next_available_boat()
calculate_daily_profit_all_boats()
