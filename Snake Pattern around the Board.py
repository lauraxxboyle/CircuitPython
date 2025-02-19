import time
from adafruit_circuitplayground import cp


snake_color = [255, 165, 0]  
cp.pixels.brightness = 0.2  
cp.pixels.auto_write = False  


num_pixels = len(cp.pixels)


snake_length = 3
snake_start = 0  

while True:
    
    snake_positions = [(snake_start + i) % num_pixels for i in range(snake_length)]
    
    
    cp.pixels.fill((0, 0, 0))

    for pos in snake_positions:
        cp.pixels[pos] = snake_color  

    cp.pixels.show()  
    time.sleep(0.5)  

    snake_start = (snake_start + 1) % num_pixels  


