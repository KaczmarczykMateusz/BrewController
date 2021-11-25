"""
Created on Nov 24 2021

@description: Class serving as API for connection with MQTT, wrapping entire logic for messages
translation and populating them in both directions. Here is the place where after running in asyncio loop
we subscribe to the broker with topics for which we'll listen. Current class is supposed to provide
numerical values to the system after receiving them in json format. In opposite direction class receives
numerical values from the system, which it translates to json and publish.

@author: Mateusz Kaczmarczyk
"""
from . import MQTTManager
import asyncio

import json


class CommunicationManager:
    mqtt_manager = None

    def __init__(self, on_set_points_received):
        """on_set_points_received: callback which will be called after message with set points is received"""
        self.on_set_points_received = on_set_points_received

    def disconnect(self):
        """Ensure it is called before program exits in order to disconnect gracefully"""
        self.mqtt_manager.disconnect_from_server()

    async def run(self):
        """Must be run in asyncio loop in order to get create new asyncio task"""
        loop = asyncio.get_running_loop()
        subscribe_topics = ["brew_controller/client_update"]
        self.mqtt_manager = MQTTManager.MQTTManager(loop, self.update_set_points, subscribe_topics)
        loop.create_task(self.mqtt_manager.run())
        await self.mqtt_manager.wait_subscribed()

    def update_set_points(self, msg):
        """Callback which will be called after receiving message with new set points value

        msg: message in json format
        """
        decoded = json.loads(msg)
        # expects string like '{"tempSp":67.5, "powerSp":85, "pumpOn":true}'
        self.on_set_points_received(decoded["tempSp"], decoded["powerSp"], decoded["pumpOn"])

    async def update_temperature(self, kettle_temp, mash_temp):
        """Publishes message to the MQTT broker

        kettle_temp, mash_temp: float values of kettle and temperatures
        """
        await self.mqtt_manager.publish_message("brew_controller/host_update",
                                                f'{{\"kettleTemp\":{kettle_temp}, \"mashTemp\":{mash_temp}}}')
