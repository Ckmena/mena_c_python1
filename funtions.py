def greetings():
	print("Hello from the greetings funtion")

#the greetings funtion just say hello 
#invoke or call the funtion
greetings()


def greetingsWithArgs(msg="a default message"):

	#print the mmsg variable
	print("Now we're saying", msg, "from another function")


greetingsWithArgs("Hey! sup!")
greetingsWithArgs("something Completely different")
greetingsWithArgs("running yet again")

#variables and scoops 
myNumberVariable = 10


#returning values from fuctions (very powerful)
def someMath(num1=2, num2=4):
	global myNumberVariable
#
	myNumberVariable = num1 + num2
	return num1 + num2



sum = someMath()
print("we are doing some math and greetings", sum)

sum = someMath(10,15)
print("another math operation with", sum, "as the result")



