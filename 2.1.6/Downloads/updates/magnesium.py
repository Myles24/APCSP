# Function to simulate actual fish tank monitoring
def get_magnesium_level():
  return 1300

def monitor():
  try:

    val1 = 1250
    val2 = 1350
    # made man_levels into a traditional list
    mag_levels = [val1, val2, 10]

    current = get_magnesium_level()
    mesg = "Magnesium level OK"

    # num_levels = len(mag_levels)
    if (current < mag_levels[0]):
      mesg = "Magnesium level too low!"
    # added elif if magnesium level is good
    elif current > mag_levels[0] and current < mag_levels[1]:
      mesg = "magnesium is good"
    # changed mag_levels to item 2 instad of the length 
    elif (current > mag_levels[1]):
      mesg = "Magnesium level too high!"
    print(mesg)
    
  except:
    print("mag")

  return mesg



