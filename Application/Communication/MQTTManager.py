"""
Created on Nov 23 2021

@description: Class responsible for connection with MQTT broker

@author: Mateusz Kaczmarczyk
"""
import uuid

import paho.mqtt.client as mqtt

import asyncio

# Some environments are requiring this (made for Spyder)
import nest_asyncio

nest_asyncio.apply()


class MQTTManager(mqtt.Client):
    subscribed = False
    client_id = 'paho-mqtt-python/issue72/' + str(uuid.uuid4())

    def __init__(self, loop, on_message_received, subscribe_topics):
        self.request_disconnect = False
        self.subscribe_topics = subscribe_topics
        self.on_message_received = on_message_received
        self.got_message = None
        self.loop = loop
        self.client = mqtt.Client(client_id=self.client_id)

        self.client.on_connect = self.on_connect
        self.client.on_connect_fail = self.on_connect_fail
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe
        self.client.on_log = self.on_log

    async def wait_subscribed(self):
        while not self.subscribed:
            await asyncio.sleep(2)

    def on_connect(self, mqttc, obj, flags, rc):
        print("Connected with return code: " + str(rc))
        for topic in self.subscribe_topics:
            self.client.subscribe(topic, 0)

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_disconnect(self, client, userdata, rc=0):
        print("Disconnected")

    def on_message(self, mqttc, obj, msg):
        self.on_message_received(msg.payload.decode("utf-8"))

    def on_publish(self, mqttc, obj, mid):
        print("message successfully published with mid code: " + str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        self.subscribed = True
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    async def run(self):
        self.client.connect('public.mqtthq.com', 1883, 60)
        self.client.loop_start()
        while not self.request_disconnect:
            await asyncio.sleep(1)

    def disconnect_from_server(self):
        self.request_disconnect = True
        self.client.disconnect()
        # TODO: investigate whi calling loop_stop here causes exception
        # self.client.loop_stop()
        self.subscribed = False

    async def publish_message(self, topic, msg):
        print("Publishing")
        self.client.publish(topic, msg, qos=1)
