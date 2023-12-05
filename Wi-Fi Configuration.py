# TASK-Digital-Watch

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
