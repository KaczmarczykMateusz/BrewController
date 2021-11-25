import asyncio

from Communication.CommunicationManager import CommunicationManager


def update_set_points(temp_sp, power_sp, pump_on):
    print(f"Set Points changed, new temp sp: {temp_sp}, new power sp: {power_sp}, new 'pump on' value: {pump_on}")


async def run():
    comm = CommunicationManager(update_set_points)
    await comm.run()
    for c in range(2):
        await comm.update_temperature(18.0, 25.0)
        await asyncio.sleep(2)
    comm.disconnect()

asyncio.run(run())
