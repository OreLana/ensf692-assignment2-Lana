# input_processing.py
# Oreoluwa Lana, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    """
    Update the status of the traffic control system based on sensor input.

    Args:
    sensor_input (int): Indicates the type of sensor input.
        - 1: Traffic light status
        - 2: Pedestrian signal status
        - 3: Vehicle detection status
    option (str): The new status value to be set.
        - For sensor_input 1: "green", "red", or "yellow"
        - For sensor_input 2 and 3: "yes" or "no"

    Raises:
    ValueError: If the option is not valid for the given sensor_input.
    """
    def update_status(self, sensor_input, option): # You may decide how to implement the arguments for this function
        if sensor_input == 1:
            if option in ["green", "red", "yellow"]:
                self.traffic_light = option
            else:
                raise ValueError("Invalid vision change")
        elif sensor_input == 2:
            if option in ["yes", "no"]:
                self.pedestrian = option
            else:
                raise ValueError("Invalid vision change")
        elif sensor_input == 3:
            if option in ["yes", "no"]:
                self.vehicle = option
            else:
                raise ValueError("Invalid vision change")



"""
Print a message based on the status of the traffic control system.

Args:
sensor: An object that contains the current status of the traffic light, pedestrian signal, and vehicle detection.
    - sensor.traffic_light (str): The current status of the traffic light ("red", "green", "yellow").
    - sensor.pedestrian (str): The current status of the pedestrian signal ("yes" or "no").
    - sensor.vehicle (str): The current status of vehicle detection ("yes" or "no").
"""
def print_message(sensor):
    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif sensor.traffic_light == "green" and sensor.pedestrian == "no" and sensor.vehicle== "no":
        print("\nProceed\n")
    elif sensor.traffic_light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\nCaution\n")
    print(f"Light = {sensor.traffic_light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .\n")


"""
Prompts the user for a sensor input and validates the input.

Returns:
    int: The validated menu choice (0, 1, 2, or 3) or None when the validation fails.
"""
def get_sensor_input():
    try:
        sensor_input = int(input("Select 1 for light, 2 for pedestrian is detected, 3 for vehicle, 0 to end the program: "))
        if sensor_input not in [0, 1, 2, 3]:
            raise ValueError
        return sensor_input
    except ValueError:
        print("You must select either 1,2,3 or 0. \n")
        return None


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    sensorApp = Sensor()
    while True:
        try:
            print("Are changes detected in the vision input?")
            sensor_input = get_sensor_input()

            if sensor_input == None:
                continue
            if sensor_input == 0:
                break
            elif sensor_input == 1:
                select_Traffic = input("What change has been identified?: ").strip()
                sensorApp.update_status(sensor_input, select_Traffic)
            elif sensor_input == 2:
                select_pedestrian = input("What change has been identified?: ").strip()
                sensorApp.update_status(sensor_input, select_pedestrian)
            elif sensor_input == 3:
                select_vehicle_status = input("What change has been identified?: ").strip()
                sensorApp.update_status(sensor_input, select_vehicle_status) 
        except ValueError as e:
            print(e)
        print_message(sensorApp)



# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

