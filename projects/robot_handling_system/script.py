from msilib.schema import Directory


class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_counter = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id` 
        DriveBot.robot_counter += 1
        self.id = DriveBot.robot_counter
        print("Creating robot #", self.id)
    
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def adjust_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def global_run(self, key):
      if key == "enable":
        DriveBot.all_disabled = True
      elif key == "disable":
        DriveBot.all_disabled = False
      else:
        print("ERROR. Invalid key.")

    def __repr__(self):
        string = \
        "Robot {id}: \n"\
        "\tMotor Speed: ..........{speed} ft/s\n"\
        "\tDirection: ............{direction} deg\n"\
        "\tSensor Range: .........{sensor} ft\n"\
        "\tLatitude, Longitude: ..({latitude}, {longitude})\n"\
        "\tRobot Engine Status: ..{all_disabled}"\
        .format(
            id = self.id,
            speed = self.motor_speed,
            direction = self.direction,
            sensor = self.sensor_range,
            latitude = self.latitude,
            longitude = self.longitude,
            all_disabled = self.all_disabled
        )
        return string


robot_1 = DriveBot(15, 50, 20)
robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

DriveBot.global_run(DriveBot, "enable")

print(robot_1)
print(robot_2)
print(robot_3)
