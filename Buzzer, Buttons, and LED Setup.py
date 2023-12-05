# TASK-Digital-Watch

# Initialize PWM for the buzzer on GPIO 25
buzzer = PWM(Pin(25), freq=440, duty=0)

# Initialize buttons
button_reset = Pin(26, Pin.IN, Pin.PULL_UP)
button_add_hour = Pin(27, Pin.IN, Pin.PULL_UP)
button_add_minute = Pin(13, Pin.IN, Pin.PULL_UP)

# Initialize LED on GPIO 3
led = Pin(3, Pin.OUT)
