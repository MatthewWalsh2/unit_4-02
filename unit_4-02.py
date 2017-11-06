#created by matthew Walsh
#created for ICS3U
#created on nov 2017
#this program rounds a number to the decimal place specified by the user


def decimal(user_input, decimal_place):
	#round number to speficied decimal place
	#process
  output = long(user_input * (10 ** decimal_place) + 0.5) / (10 ** decimal_place)
  #output
  print(str(output))

#input
user_input = raw_input("Type a decimal number: ")
user_input = float(user_input)
decimal_place = raw_input("Type how many decimal places you want to round the number: ")
decimal_place = float(decimal_place)
decimal(user_input, decimal_place)
