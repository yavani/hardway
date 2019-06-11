cars = 100  # no of cars

space_in_car = 4 # space in each car it can be floting point as well

drivers = 30 # drivers for car

passengers = 90 # no of passengers

cars_not_driven = cars- passengers # counts cars not driven

cars_driven = drivers # cars driven is same as number of avilable drivers

carpool_capacity = cars_driven * space_in_car # calculate the carpool capacity

average_passengers_per_car = passengers/ cars_driven # calculate average passengers per car

print("there are", cars ,"cars available") # print the above calculations below

print("there are only", drivers , "drivers available")

print("there will be",cars_not_driven, "empty cars today")

print("we can transport" ,carpool_capacity ,"people today")

print("we have", passengers,"to carpool today")

print("we need to put about", average_passengers_per_car ,"in each car .")

