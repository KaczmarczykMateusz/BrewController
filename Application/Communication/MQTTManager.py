"""
Created on Nov 23 2021

@author: Mateusz Kaczmarczyk
"""
import uuid

import paho.mqtt.client as mqtt

import asyncio

#Somne environments are requiring this (made for Spyder)
import nest_asyncio
nest_asyncio.apply()


class MQTTManager(mqtt.Client):
    topic = "brew_controller/host_update"
    subscribed = False
    client_id = 'paho-mqtt-python/issue72/' + str(uuid.uuid4())
    
    def __init__(self, loop):
        self.got_message = None
        self.loop = loop
        self.client = mqtt.Client(client_id=self.client_id)
        
        self.client.on_connect = self.on_connect
        self.client.on_connect_fail = self.on_connect_fail
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe
        self.client.on_log = self.on_log

    async def wait_subscribed(self):
        while not self.subscribed:
            await asyncio.sleep(2)  
        return            
    
    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))
        self.client.subscribe(self.topic, 0)

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_message(self, mqttc, obj, msg):
        if not self.got_message:
            print("Received unexpected message: " + str(msg.payload.decode("utf-8")))#{}".format(msg.decode()))
        else:
            self.got_message.set_result(msg.payload)

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        self.subscribed = True
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    async def run(self):
        self.client.connect('public.mqtthq.com', 1883, 60)
        
        self.client.loop_start()
        while True:
            await asyncio.sleep(2)
    
    def disconnect_from_server(self):
        self.client.disconnect()
        
    async def publish_message(self, msg):
        print("Publishing")
        self.got_message = self.loop.create_future()
        self.client.publish(self.topic, msg, qos=1)
        msg = await self.got_message
        print("Got response with {} bytes".format(len(msg)))
        self.got_message = None

