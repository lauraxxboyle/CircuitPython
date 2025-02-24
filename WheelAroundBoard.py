import time
from adafruit_circuitplayground import cp

#Setup
blue = [0, 100, 255]  #RGB values for blue color
cp.pixels.brightness = 0.2
pixels_length = len(cp.pixels)


# Continuous loop
while True:  
    # Iterate through each pixel and light it up one by one
    for pixel in range(pixels_length):
        cp.pixels[pixel] = blue
        time.sleep(0.3)  # Short delay
    
    # Turn off all pixels after the loop
    cp.pixels.fill([0, 0, 0])
    time.sleep(0.3)
