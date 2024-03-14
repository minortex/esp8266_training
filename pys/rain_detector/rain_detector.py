from umqtt.simple import MQTTClient
from machine import Pin
import time

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

while True:
    rain_status = check_rain(rain_sensor)
    send_mqtt(mqtt_client, mqtt_topic, rain_status)
    time.sleep(5)  # wait for 5 seconds
