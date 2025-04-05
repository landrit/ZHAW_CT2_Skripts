"""
INPUT
"""

TIM_ARR = 0x9C3F  # auto reload register value in hex (0xbb80 = 48000)
ARR = 40000
counter_mode = "UPCOUNTER"  # "UPCOUNTER" or "DOWNCOUNTER"
TARGET_DUTY_CYCLE = 25

"""
END INPUT
"""

# Convert hex to decimal if provided
if TIM_ARR is not None:
    ARR = TIM_ARR

# Calculate the new ARR based on the duty cycle
new_ARR = ARR * (TARGET_DUTY_CYCLE / 100)

# Round the new ARR to the nearest integer as it should be an integer
new_ARR = round(new_ARR)

# Depending on the counter mode, calculate the counter value
if counter_mode == "UPCOUNTER":
    counter_value = new_ARR
elif counter_mode == "DOWNCOUNTER":
    counter_value = ARR - new_ARR

else:
    counter_value = None
    print("Invalid counter mode.")

# Print the counter value
if counter_value is not None:
    print(f'The counter value for a {TARGET_DUTY_CYCLE}% duty cycle is {hex(counter_value)} ({counter_value} - 1).')
