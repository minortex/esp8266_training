from umqtt.simple import MQTTClient

SERVER = "v.texsd.eu.org:1883"
TOPIC = "home/room/rainDetector"

def main(server=SERVER):
    c = MQTTClient("umqtt_client", server) # 创建一个MQTT客户端
    c.connect() # 连接到MQTT服务器
    while True:
        if True: # 这里替代成你实际检测雨滴的条件
            c.publish(TOPIC, "rain detected") #如果检测到雨滴，发布消息到特定主题
    c.disconnect() # 断开连接
