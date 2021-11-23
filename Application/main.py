from Communication import MQTTManager
import asyncio

async def mainLoop():
    #Test MQTTManager
    loop = asyncio.get_running_loop()
    mqtt_manager = MQTTManager.MQTTManager(loop)
    loop.create_task(mqtt_manager.run())
    await mqtt_manager.wait_subscribed()
    for c in range(2):
        await mqtt_manager.publish_message('{\"kettleTemp\":18.0, \"mashTemp\":25.0}');
        await asyncio.sleep(2)
    mqtt_manager.disconnect_from_server()
    
asyncio.run(mainLoop())

