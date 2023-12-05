
## Digital Clock Project Using ESP32 and MicroPython

### Overview
This project involves the design and implementation of a digital clock using MicroPython on the ESP32 microcontroller. The clock displays time in both decimal and binary formats and includes features such as alarm functionality and synchronization with network time servers.

### Features
- **Wi-Fi Connectivity**: Connects to Wi-Fi for network time synchronization.
- **NTP Time Synchronization**: Uses NTP to keep the time accurate.
- **OLED and TM1637 Display**: Shows time in decimal (TM1637) and binary (OLED) formats.
- **Alarm Functionality**: Set, reset, and modify alarm times.
- **User Interaction**: Buttons for alarm adjustments and reset.
- **Visual and Audio Indicators**: LED for synchronization status and buzzer for alarms.

### Hardware Components
- ESP32 Microcontroller
- SH1106 OLED Display
- TM1637 Digital Tube Display
- Buzzer
- Buttons
- LED
- Resistors and connecting wires

### Software Setup
1. **Importing Libraries**: Necessary MicroPython libraries are used for controlling hardware components and time management.
2. **Wi-Fi Connection Setup**: The ESP32 is configured to connect to a Wi-Fi network.
3. **Time Synchronization**: The ESP32's internal clock is synchronized with an NTP server (`time.google.com`).
4. **Display Initialization**: Initialization of OLED and TM1637 displays using I2C and GPIO pins respectively.
5. **Buzzer and Button Setup**: Configuration of a PWM buzzer for alarms and buttons for user interaction.
6. **Alarm Settings**: Initialize and manage alarm settings.

### Functionality
- **Displaying Time**: Time is displayed in both binary format on the OLED and decimal format on the TM1637 display.
- **Alarm Management**: Functions to reset, set, and adjust alarm times, with real-time display updates.
- **Synchronization Indicator**: An LED blinks to indicate successful synchronization with the NTP server.
- **Alarm Notification**: The buzzer sounds when the alarm time is reached.
- **Time Synchronization**: Periodic synchronization with the NTP server to ensure accuracy.

### Usage
- Set the correct Wi-Fi credentials for time synchronization.
- Use the buttons to set and adjust the alarm time.
- The clock will display the current time and the set alarm time.
- Buzzer sounds at the set alarm time.

### Code Structure
The code is structured into various sections for ease of understanding and modification. Each component (Wi-Fi, display, buzzer, buttons) is initialized and controlled in separate sections.
