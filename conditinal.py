# print a message to the terminal window
print("rules that govern the state of water")

# set up a variable to hold the temperature we input
current_temp = False

while current_temp is False:
# make this a number and clean the code up (dry it out)
    current_temp = input("enter a temperature:\n")

    # see what current tempeture is
    print("you input", current_temp)


# if the current temp ia at freezing or below, water is solid
    if (int(current_temp) < 0 or (int(current_temp) == 0)):
       print("water is a solid! cuz it's at or below freezing")
       current_temp = False


# else check anaother condition, if it's not freezing, is below boiling?    
    elif (int(current_temp)< 100):
         print("water is a liquid, because It's above freezing and below boiling")
         current_temp = False

    elif (int(current_temp) > 100 or (int(current_temp) == 100)):
         print("water is a gas, cuz it's, like really hot")
         current_temp = False