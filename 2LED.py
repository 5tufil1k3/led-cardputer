from machine import Pin
from time import sleep
from neopixel import NeoPixel
import urandom

# Pin definitions
PIN_BUTTON = 0
PIN_LED = 21
NUM_LEDS = 1

# LED status values
RAINBOW = 0
RED = 1
GREEN = 2
BLUE = 3

# Initialize NeoPixel
np = NeoPixel(Pin(PIN_LED, Pin.OUT), NUM_LEDS)

# Initialize button pin
button = Pin(PIN_BUTTON, Pin.IN, Pin.PULL_UP)

# LED status strings
led_status_string = ["Rainbow", "Red", "Green", "Blue"]

# Initialize LED status and color
led_status = RAINBOW
led_color = (0, 0, 0)

# Delay for rainbow effect
RAINBOW_DELAY = 0.5  # in seconds

# Main loop
while True:
    # Update LED color based on LED status
    if led_status == RAINBOW:
        # Generate random color for rainbow effect
        led_color = (urandom.randint(0, 255), urandom.randint(0, 255), urandom.randint(0, 255))
    elif led_status == RED:
        led_color = (255, 0, 0)
    elif led_status == GREEN:
        led_color = (0, 255, 0)
    elif led_status == BLUE:
        led_color = (0, 0, 255)

    # Update LED
    np[0] = led_color
    np.write()

    # Check button press to change LED status
    if not button.value():
        sleep(0.05)  # Debouncing delay
        if not button.value():
            led_status += 1
            if led_status > BLUE:
                led_status = RAINBOW
            while not button.value():
                pass  # Wait for button release
            print("LED status updated:", led_status_string[led_status])

    # Add delay for rainbow effect
    if led_status == RAINBOW:
        sleep(RAINBOW_DELAY)
