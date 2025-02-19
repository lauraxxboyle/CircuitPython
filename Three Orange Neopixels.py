import time
from adafruit_circuitplayground import cp

orange = [200, 70, 0]  
pixels_off_state = [0, 0, 0]  
cp.pixels.brightness = 0.2  
cp.pixels.auto_write = False 


pixel_indices = [3, 4, 5] 

while True:
   
    for i in pixel_indices:
        cp.pixels[i] = orange  
    
    cp.pixels.show()  
    time.sleep(1)  

    
    for i in pixel_indices:
        cp.pixels[i] = pixels_off_state  

    cp.pixels.show()  
    time.sleep(1)  


