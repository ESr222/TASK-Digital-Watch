import machine
import time
import network
import ntptime
from machine import Pin, I2C, PWM
import sh1106
import tm1637

# Wi-Fi credentials
ssid = 'iPhone de Emilio'
password = '12345678'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print("Connected to WiFi")

# Set the NTP server to time.google.com
ntptime.host = 'time.google.com'

# Adjust for Spanish timezone (UTC+1 or UTC+2 for daylight saving)
time_offset = 3600  # Change this as needed

# Initialize OLED display
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled_display = sh1106.SH1106_I2C(128, 64, i2c)

# Initialize TM1637 display
CLK = Pin(23)  # Replace with your actual pin
DIO = Pin(5)   # Replace with your actual pin
tm_display = tm1637.TM1637(clk=CLK, dio=DIO)

# Initialize PWM for the buzzer on GPIO 25
buzzer = PWM(Pin(25), freq=440, duty=0)  # Start with the buzzer turned off

# Initialize buttons
button_reset = Pin(26, Pin.IN, Pin.PULL_UP)  # Botón S1-A1 para resetear alarma
button_add_hour = Pin(27, Pin.IN, Pin.PULL_UP)  # Botón S2-A2 para agregar hora
button_add_minute = Pin(13, Pin.IN, Pin.PULL_UP)  # Botón S3-A3 para agregar minutos

# Initialize LED on GPIO 3
led = Pin(3, Pin.OUT)

# Alarm variables
alarm_hour = 18  # Initial alarm hour
alarm_minute = 31  # Initial alarm minute
alarm_set = False  # Flag to indicate if the alarm is set

def display_binary_time(hour, minute, second):
    """Displays the current time in binary format on the OLED screen."""
    hour_bin = "{:08b}".format(hour)
    minute_bin = "{:08b}".format(minute)
    second_bin = "{:08b}".format(second)

    oled_display.fill(0)
    oled_display.text('<-H',80,0)
    oled_display.text('<-Min',80,16)
    oled_display.text('<-Sec',80,32)
    """Displays the alarm time on the OLED screen."""
    oled_display.text("Alarm:{:02d}:{:02d}".format(alarm_hour, alarm_minute), 0, 48)
    
    for i in range(8):
        oled_display.text('*' if hour_bin[i] == '1' else '_', 10 * i, 0)
        oled_display.text('*' if minute_bin[i] == '1' else '_', 10 * i, 16)
        oled_display.text('*' if second_bin[i] == '1' else '_', 10 * i, 32)
    oled_display.show()

def reset_alarm(pin):
    global alarm_set
    alarm_set = False  # Reset the alarm flag
    display_binary_time(hour,minute,second)  # Update OLED screen

def add_hour(pin):
    global alarm_hour, alarm_set
    alarm_hour = (alarm_hour + 1) % 24
    alarm_set = False  # Reset alarm state
    display_binary_time(hour,minute,second)  # Update OLED screen

def add_minute(pin):
    global alarm_minute, alarm_set
    alarm_minute = (alarm_minute + 1) % 60
    alarm_set = False  # Reset alarm state
    display_binary_time(hour,minute,second)  # Update OLED screen

# Set up button interrupts
button_reset.irq(trigger=Pin.IRQ_FALLING, handler=reset_alarm)
button_add_hour.irq(trigger=Pin.IRQ_FALLING, handler=add_hour)
button_add_minute.irq(trigger=Pin.IRQ_FALLING, handler=add_minute)

def sound_buzzer(freq, duration):
    buzzer.init(freq=freq, duty=512)  # Reinitialize the buzzer
    time.sleep(duration)
    buzzer.deinit()  # Deinitialize the buzzer to stop it

def sync_time():
    """Syncs time with NTP server and blinks the LED."""
    led.value(1)  # Turn on LED
    ntptime.settime()
    led.value(0)  # Turn off LED

# Sync time immediately after Wi-Fi connection
sync_time()

# Main loop
dots = False
last_sync_time = time.time()
sync_interval = 600  # Set sync interval (e.g., 600 seconds for 10 minutes)

while True:
    current_time = time.time()
    year, month, mday, hour, minute, second, weekday, yearday = time.localtime(current_time + time_offset)

    # Sync time with NTP server every sync_interval seconds
    if current_time - last_sync_time >= sync_interval:
        sync_time()
        last_sync_time = current_time

    # Display time with blinking dots on TM1637
    tm_display.numbers(hour, minute, dots)
    dots = not dots  # Toggle dots for blinking effect

    # Always display the alarm time on the OLED screen
    display_binary_time(hour, minute, second)

    # Check if it's the alarm time and if it has not been deactivated
    if not alarm_set and hour == alarm_hour and minute == alarm_minute:
        sound_buzzer(1000, 10)  # Sound the buzzer for 10 seconds
        alarm_set = True  # Set the alarm flag

    time.sleep(1)  # Sleep for a second before next iteration
