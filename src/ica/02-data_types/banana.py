#define variables
banana_length = 15.5
num_bananas = 5100

#calculate total length in cm
total_length_cm = banana_length * num_bananas

#convert to meters (dividing by 100)
total_length_meters = total_length_cm / 100

print("Total length of", num_bananas, "bananas:", total_length_meters, "meters")