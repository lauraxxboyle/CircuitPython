import time
from adafruit_circuitplayground import cp

blue = [0, 0, 255]  # Blue color
pixels_off_state = [0, 0, 0]  # Turn pixel off
cp.pixels.brightness = 0.2  # Set brightness

while True:
    cp.pixels[6] = blue  # Turn pixel 6 blue
    cp.pixels.show()  # Ensure the change is displayed
    time.sleep(0.5)  # Keep it on for 0.5 seconds

    cp.pixels[6] = pixels_off_state  # Turn pixel 6 off
    cp.pixels.show()  # Update display
    time.sleep(9.5)  # Keep it off for 9.5 seconds