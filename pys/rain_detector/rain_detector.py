from umqtt.simple import MQTTClient
from machine import Pin
import time
import network

# 配网
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# sta_if.scan()
sta_if.connect("k30su", "123456879")
while not sta_if.isconnected() == 0:
    print("connecting.")
print(sta_if.ifconfig())

# MQTT服务器的IP地址
mqtt_server = 'v.texsd.eu.org'
client_id = 'esp8266'
mqtt_topic = 'rain_detector'

# 雨滴传感器连接的引脚
rain_pin = 14
rain_sensor = Pin(rain_pin, Pin.IN)

def connect_mqtt():
    client = MQTTClient(client_id, mqtt_server)
    client.connect()
    print('Connected to %s MQTT broker' % mqtt_server)
    return client

def check_rain(sensor):
    state = sensor.value()
    if state == 0:
        return 'True'
    else:
        return 'False'

def send_mqtt(client, topic, message):
    client.publish(topic, message)

mqtt_client = connect_mqtt()

# 初始化上一次的雨滴状态
last_rain_status = None

while True:
    rain_status = check_rain(rain_sensor)
    # 检查雨滴状态是否发生变化
    if rain_status != last_rain_status:
        send_mqtt(mqtt_client, mqtt_topic, rain_status)
        # 更新上一次的雨滴状态
        last_rain_status = rain_status
    time.sleep(5)  # 5s后重新探测

