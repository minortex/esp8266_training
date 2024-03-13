from machine import Pin, I2C
import ssd1306
import dht
dht11 = dht.DHT11(Pin(5))
dht11.measure()
temp = dht11.temperature()
hum = dht11.humidity()
print(hum)
oled = ssd1306.SSD1306_I2C(128,64,I2C(scl=Pin(14), sda=Pin(2)))
oled.fill(0)
oled.text(f'temperature:{temp}', 10, 10)
oled.text(f'humidity:{hum}', 10, 30)
oled.text('B23011131', 10, 50)
oled.show()

