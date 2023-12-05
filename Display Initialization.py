# TASK-Digital-Watch

# Initialize OLED display
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled_display = sh1106.SH1106_I2C(128, 64, i2c)

# Initialize TM1637 display
CLK = Pin(23)
DIO = Pin(5)
tm_display = tm1637.TM1637(clk=CLK, dio=DIO)
