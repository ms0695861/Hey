#Temperature Conversion
#Let user enter the "Celsius"
#And print to "Fahrenheit"
temp_c = input('Please enter the Celsius: ') 
temp_c = float(temp_c) #str convert to float
temp_f = (9 / 5 * temp_c) + 32 
print('Fahrenheit is: ', temp_f)

