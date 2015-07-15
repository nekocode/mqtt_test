__author__ = 'nekocode'

import datetime

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("MQTT client not find. Please install as follow:")
    print("git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git")
    print("cd org.eclipse.paho.mqtt.python")
    print("sudo python setup.py install")


def on_connect(mqttc, obj, rc):
    print("OnConnetc, rc: " + str(rc))


def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print("Log:" + string)


def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    on_exec(str(msg.payload))


def on_exec(strcmd):
    print "Exec:", strcmd


# =====================================================
if __name__ == '__main__':
    client = mqtt.Client("mynodeserver")
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe
    client.on_log = on_log

    # strBroker = "localhost"
    broker = "mosquitto.org"

    client.connect(broker)
    client.subscribe("/inode/mychannel", 0)
    client.loop_forever()
