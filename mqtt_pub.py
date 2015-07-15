__author__ = 'nekocode'

# !/usr/bin/python
# This shows a service of an MQTT subscriber.
# Copyright (c) 2010-2015, By openthings@163.com.

import paho.mqtt.publish as publish


def transmit_mqtt(msg):
    # strMqttBroker = "localhost"
    mqtt_broker = "mosquitto.org"
    mqtt_channel = "/inode/mychannel"
    print(msg)
    publish.single(mqtt_channel, msg, hostname=mqtt_broker)


if __name__ == '__main__':
    transmit_mqtt("Hello,MQTT Proxy, I am client inside python.")
    print "Send msg ok."
