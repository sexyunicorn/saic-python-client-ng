import asyncio
import logging
import sys
import os
import config as c

from saic_ismart_client_ng import SaicApi
from saic_ismart_client_ng.model import SaicApiConfiguration


async def main():
    config = SaicApiConfiguration(
        username=c.username,
        password=c.password,
        username_is_email=True,
        base_uri="https://gateway-mg-au.soimt.com/api.app/v1/",
        tenant_id="459771",
        region="au",
        sms_delivery_delay=3,
    )
    
    saic_api = SaicApi(config)
    await saic_api.login()
    print(c.vin)
    # vehicle_status = await saic_api.get_vehicle_status(vin)
    # print(vehicle_status)
    # logging.info("Auth token expires at %s", saic_api.token_expiration)
    # vehicle_list_rest = await saic_api.vehicle_list()
    # print("-----------------")
    # print(vehicle_list_rest)
    # while True:
    #     cars = vehicle_list_rest.vinList
    #     for car in cars:
    #         vin_num = car.vin
    #         vehicle_status = await saic_api.get_vehicle_status(vin_num)
    #         # logging.info("Battery voltage is %d", vehicle_status.basicVehicleStatus.batteryVoltage)
    #         # charging_status = await saic_api.get_vehicle_charging_management_data(vin_num)
    #         # logging.info("Current power is %d", charging_status.rvsChargeStatus.realtimePower)
    #         # logging.info("My VIN is %s", vin_num)
    #     await asyncio.sleep(10)


if __name__ == "__main__":
    global should_debug
    debug_envvar = str(os.environ.get("DEBUG"))
    if debug_envvar.lower() == "true":
        should_debug = True
        log_level = logging.DEBUG
    else:
        should_debug = False
        log_level = logging.INFO
    logging.basicConfig(
        stream=sys.stdout,
        format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=log_level,
    )
    logging.debug("should_debug is %s", should_debug)

    asyncio.run(main())
