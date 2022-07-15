def monitor():
  try:

    temps = [50, 55, 60, 65, 70, 75]

    mesg = "Temperature OK"

    # get multiple temperature readings
    temp_readings = get_temps()
    # added a procedure that gets number of items in temps list for average
    num_readings = len(temp_readings)

    # sum adds up all items in list
    # combined line 16 and 15
    ave_temp = sum(temp_readings) / num_readings
    # ave_temp = ave_temp / num_readings

    if (ave_temp < temps[0]):
      mesg = "Average temperature too cold!"
    # added an elif statement that calculates if the temperature is good
    elif ave_temp > temps[0] and ave_temp < temps[5]:
      mesg = ("Temperature is good")
    elif (ave_temp > temps[5]):
      mesg = "Average temperature too warm!"
    print(mesg)
  except:
    print("temp")

  return mesg

def get_temps():
  return [55, 65, 70]

