import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# sta_if.scan()
sta_if.connect("p_2.4", "12345687") # Connect to an AP
while not sta_if.isconnected() == 0:
    print("connecting.")                      # Check for successful connection
print(sta_if.ifconfig())