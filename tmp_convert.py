#Temperature Conversion
#Let user enter the "Celsius"
#And print to "Fahrenheit"
temp_c = input('Please enter the Temperature: ')
temp_c = int(temp_c) #str convert to int
temp_f = (9/5*temp_c)+32
print(temp_f)
