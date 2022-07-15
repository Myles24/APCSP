def monitor():
  try:
    
    val1 = 17
    val2 = 12

    # made alkilines into a traditional list
    alkilines = [val1, val2+1]

    current = get_alkalinity()
    mesg = "Alkalinity OK"
    # changed the item number to 1 (the smaller value)
    if (current < alkilines[1]):
      mesg = "Alkalinity too low!"
    # added elif statement that determines if alkalinity is good
    elif current > alkilines[1] and current < alkilines[0]:
      mesg = ("alkilinity is good")
    # changed the item number from 5 to 0 (the larger value)
    elif (current > alkilines[0]):
      mesg = "Alkalinity too high!"
    print(mesg)
    
  except:
    print("alk") 
    
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  return 9

