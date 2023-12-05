def reset_alarm(pin):
    # Function to reset alarm
    ...

def add_hour(pin):
    # Function to add an hour to the alarm
    ...

def add_minute(pin):
    # Function to add a minute to the alarm
    ...

# Set up button interrupts
button_reset.irq(trigger=Pin.IRQ_FALLING, handler=reset_alarm)
button_add_hour.irq(trigger=Pin.IRQ_FALLING, handler=add_hour)
button_add_minute.irq(trigger=Pin.IRQ_FALLING, handler=add_minute)

def sound_buzzer(freq, duration):
    # Function to sound the buzzer
    ...
